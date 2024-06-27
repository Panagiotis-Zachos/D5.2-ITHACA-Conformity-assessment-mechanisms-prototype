import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
import shutil
from models import create_model, PrivacyMetricsCallback
from tensorflow_privacy.privacy.privacy_tests.membership_inference_attack import (
    privacy_report,
)
from tensorflow_privacy.privacy.privacy_tests.membership_inference_attack.data_structures import (
    PrivacyMetric,
    AttackResultsCollection,
)
from sklearn.model_selection import train_test_split
import tensorflow as tf

data_df = pd.read_csv("data/synthetic_fairness_dataset.csv")
data_df.head()

# Shuffle training dataframe
data_df = data_df.sample(
    frac=1, random_state=42
)  # shuffle with random_state=42 for reproducibility

X = [re.sub("http://\S+|https://\S+", "", text) for text in data_df["tweet"]]
X = np.array(X)
vul = np.array(data_df["vulnerability"])
vul = vul.reshape(vul.shape[0], 1)
toxicity = np.array(data_df["Toxicity"])
toxicity = toxicity.reshape(toxicity.shape[0], 1)
y = np.concatenate([toxicity, vul], axis=1)

(
    train_sentences,
    val_sentences,
    train_labels_plus_vul,
    val_labels_plus_vul,
) = train_test_split(
    X, y, test_size=0.20, random_state=42
)  # dedicate 20% of samples to validation set

train_labels = train_labels_plus_vul[:, 0]
train_labels = train_labels.reshape(train_labels.shape[0], 1)
val_labels = val_labels_plus_vul[:, 0]
al_labels = val_labels.reshape(val_labels.shape[0], 1)

train_sentences = np.array(train_sentences)

tf.random.set_seed(42)

checkpoint_path = "./models/normal_model/model.{epoch:02d}-{val_loss:.4f}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
if not os.path.exists(checkpoint_dir):
    os.makedirs(checkpoint_dir)  # Create directory if it doesn't exist
else:
    shutil.rmtree(checkpoint_dir)  # Remove directory to start new experiment
    os.makedirs(checkpoint_dir)

model_1 = create_model(train_sentences)
model_1.summary()

model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    save_weights_only=True,
    save_freq="epoch",
    monitor="val_accuracy",
    mode="max",
    verbose=1,
    save_best_only=True,
)

BATCH_SIZE = 1024
epochs_per_report = 1
privacy_callback = PrivacyMetricsCallback(
    epochs_per_report,
    train_sentences,
    val_sentences,
    train_labels,
    val_labels,
    BATCH_SIZE,
    "Model 1",
)

all_reports = []
history_1 = model_1.fit(
    train_sentences,
    train_labels,
    epochs=50,
    validation_data=(val_sentences, np.array(val_labels)),
    callbacks=[model_checkpoint_callback, privacy_callback],
    batch_size=BATCH_SIZE
)
all_reports.extend(privacy_callback.attack_results)
results = AttackResultsCollection(all_reports)
privacy_metrics = (
    PrivacyMetric.AUC,
    PrivacyMetric.ATTACKER_ADVANTAGE,
    PrivacyMetric.PPV,
)
epoch_plot = privacy_report.plot_by_epochs(results, privacy_metrics=privacy_metrics)

if not os.path.exists('./results/normal_model/'):
    os.makedirs('./results/normal_model/')  # Create directory if it doesn't exist
else:
    shutil.rmtree('./results/normal_model/')  # Remove directory to start new experiment
    os.makedirs('./results/normal_model/')
results.save('./results/normal_model/')

plt.show()

# best = tf.train.latest_checkpoint(
#     checkpoint_dir
# )  # Since save_best_only=True, latest model is also the best
# model_1.load_weights(best)
# model_1_evaluate = model_1.evaluate(val_sentences, val_labels)


def plot_graphs(history, string):
    plt.plot(history.history[string])
    plt.plot(history.history["val_" + string])
    plt.xlabel("Epochs")
    plt.ylabel(string)
    plt.legend([string, "val_" + string])
    plt.show()


plot_graphs(history_1, "accuracy")
plot_graphs(history_1, "loss")
