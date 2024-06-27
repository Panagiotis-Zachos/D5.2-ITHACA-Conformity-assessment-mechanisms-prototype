import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
import shutil
from models import create_dp_model, PrivacyMetricsCallback

from sklearn.model_selection import train_test_split
import tensorflow as tf

from tensorflow_privacy.privacy.analysis import (
    compute_dp_sgd_privacy_lib as compute_dp_sgd_privacy,
)

from tensorflow_privacy.privacy.privacy_tests.membership_inference_attack import (
    privacy_report,
)
from tensorflow_privacy.privacy.privacy_tests.membership_inference_attack.data_structures import (
    PrivacyMetric,
    AttackResultsCollection,
)

# from tensorflow_privacy.privacy.privacy_tests.membership_inference_attack import (
#     privacy_report,
# )


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
tf.get_logger().setLevel("ERROR")
tf.random.set_seed(42)

checkpoint_path = (
    "./models/differentially_private/model.{epoch:02d}-{val_accuracy:.4f}.ckpt"
)
checkpoint_dir = os.path.dirname(checkpoint_path)
if not os.path.exists(checkpoint_dir):
    os.makedirs(checkpoint_dir)  # Create directory if it doesn't exist
else:
    shutil.rmtree(checkpoint_dir)  # Remove directory to start new experiment
    os.makedirs(checkpoint_dir)

model_1 = create_dp_model(train_sentences)
# model_1.summary()

model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    save_weights_only=True,
    save_freq="epoch",
    monitor="val_accuracy",
    mode="max",
    verbose=1,
    save_best_only=True,
)

EPOCHS = 200
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

lr_scheduler_callback = tf.keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=15, verbose=1,cooldown=5, min_lr=1e-6)

early_stopping_callback = tf.keras.callbacks.EarlyStopping(
    monitor="val_accuracy", patience=10, start_from_epoch=20, verbose=1, mode="max"
)

all_reports = []

'''
The following code snippet includes various function calls and operations related to training a machine learning model with privacy guarantees.

The first part of the code snippet shows the training process using the fit() function of a model_1 object. The fit() function takes in training data (train_sentences and train_labels), as well as other parameters such as the number of epochs, validation data, callbacks, batch size, and shuffle flag. This function trains the model and returns a history object that contains information about the training process.

Next, the code snippet retrieves the latest checkpoint of the trained model using the tf.train.latest_checkpoint() function. The checkpoint_dir parameter specifies the directory where the model checkpoints are saved. The latest checkpoint is loaded into the model_1 object using the load_weights() function.

After loading the best model, the code snippet evaluates the model's performance on the validation data using the evaluate() function of model_1. The evaluation results are stored in the model_1_evaluate variable.

The code then calls the compute_dp_sgd_privacy.compute_dp_sgd_privacy_statement() function to compute and print a privacy statement. This function takes in various parameters such as the number of training examples, number of epochs, batch size, noise multiplier, and delta. It calculates the privacy guarantee provided by the differentially private stochastic gradient descent (DP-SGD) algorithm used for training the model.

Next, the code snippet creates an AttackResultsCollection object called results to store the attack results. The AttackResultsCollection class is a collection of AttackResults objects, which store the results of privacy attacks on the trained model.

The code snippet then defines a list of privacy metrics (privacy_metrics) that will be used for plotting the privacy vulnerabilities. It also calls the plot_by_epochs() function to generate a plot showing the privacy vulnerabilities over the epochs of training. The plot includes multiple subplots, each representing a different privacy metric.

The code snippet checks if a directory named ./results/dp_model/ exists. If it doesn't exist, the code creates the directory using the os.makedirs() function. If the directory already exists, it is removed using shutil.rmtree() and then recreated.

Finally, the code snippet saves the results object to the ./results/dp_model/ directory using the save() method of the AttackResultsCollection class. The save() method serializes the object and saves it to a pickle file.

The code snippet concludes by calling plt.show() to display the generated plot of accuracy and loss over the epochs.
'''

history_1 = model_1.fit(
    train_sentences,
    train_labels,
    epochs=EPOCHS,
    validation_data=(val_sentences, np.array(val_labels)),
    callbacks=[
        model_checkpoint_callback,
        privacy_callback,
        early_stopping_callback,
        lr_scheduler_callback,
    ],
    batch_size=BATCH_SIZE,
    shuffle=True,
)
all_reports.extend(privacy_callback.attack_results)

best = tf.train.latest_checkpoint(
    checkpoint_dir
)  # Since save_best_only=True, latest model is also the best
model_1.load_weights(best)
model_1_evaluate = model_1.evaluate(val_sentences, val_labels)
print(
    compute_dp_sgd_privacy.compute_dp_sgd_privacy_statement(
        number_of_examples=train_sentences.shape[0],
        num_epochs=int(best.split('-')[0].split('.')[-1]),
        batch_size=BATCH_SIZE,
        noise_multiplier=1.0,  # found in models.py completely incorrect way to do this but works
        delta=1e-5,
        used_microbatching=False,
    )
)

results = AttackResultsCollection(all_reports)

privacy_metrics = (
    PrivacyMetric.AUC,  # https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
    PrivacyMetric.ATTACKER_ADVANTAGE,
    PrivacyMetric.PPV,
)  # AUC, ATTACKER_ADVANTAGE, PPV, EPSILON_LOWER_BOUND
epoch_plot = privacy_report.plot_by_epochs(results, privacy_metrics=privacy_metrics)

if not os.path.exists('./results/dp_model/'):
    os.makedirs('./results/dp_model/')  # Create directory if it doesn't exist
else:
    shutil.rmtree('./results/dp_model/')  # Remove directory to start new experiment
    os.makedirs('./results/dp_model/')
results.save('./results/dp_model/')

plt.show()

def plot_graphs(history, string):
    plt.plot(history.history[string])
    plt.plot(history.history["val_" + string])
    plt.xlabel("Epochs")
    plt.ylabel(string)
    plt.legend([string, "val_" + string])
    plt.show()


plot_graphs(history_1, "accuracy")
plot_graphs(history_1, "loss")

