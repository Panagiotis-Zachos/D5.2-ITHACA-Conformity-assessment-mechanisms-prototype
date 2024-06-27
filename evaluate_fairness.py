import tensorflow as tf
import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import ClassificationMetric
from aif360.sklearn.metrics import between_group_generalized_entropy_error
from models import create_model

checkpoint_dir = "./models/normal_model"


def load_model(checkpoint_directory):
    """
    Loads a trained model from a checkpoint directory.

    Args:
        checkpoint_directory (str): The directory path where the model checkpoints are stored.

    Returns:
        model: The loaded model with weights restored from the best checkpoint.

    Example:
        >>> model = load_model("./path/to/model/")
    """
    model = create_model()
    best_checkpoint = tf.train.latest_checkpoint(checkpoint_directory)
    model.load_weights(best_checkpoint)
    return model


def preprocess_data(data_df):
    """
    Preprocesses the data by shuffling the dataframe, removing URLs from tweets,
    and preparing the input and target arrays for training.

    Args:
        data_df (pandas.DataFrame): The input data dataframe.

    Returns:
        tuple: A tuple containing the preprocessed input array (X) and target array (y).

    Example:
        >>> data = pd.read_csv("path/to/dataset")
        >>> X, y = preprocess_data(data)
    """
    data_df = data_df.sample(frac=1, random_state=42)
    X = [re.sub("http://\S+|https://\S+", "", text) for text in data_df["tweet"]]
    X = np.array(X)
    vul = np.array(data_df["vulnerability"]).reshape(-1, 1)
    toxicity = np.array(data_df["Toxicity"]).reshape(-1, 1)
    y = np.concatenate([toxicity, vul], axis=1)
    return X, y


def split_data(X, y):
    """
    Split the data into training and validation sets.

    Args:
        X (array-like): The input features.
        y (array-like): The target labels.

    Returns:
        tuple: A tuple containing the training sentences, validation sentences,
               training labels plus vulnerability, and validation labels plus vulnerability.

    Example:
        >>> data = pd.read_csv("path/to/dataset")
        >>> X, y = preprocess_data(data)
        >>> train_sentences, val_sentences, train_labels_plus_vul, val_labels_plus_vul = split_data(X, y)
        >>> print("Training sentences:", train_sentences)
        >>> print("Validation sentences:", val_sentences)
        >>> print("Training labels plus vulnerability:", train_labels_plus_vul)
        >>> print("Validation labels plus vulnerability:", val_labels_plus_vul)
    """
    (
        train_sentences,
        val_sentences,
        train_labels_plus_vul,
        val_labels_plus_vul,
    ) = train_test_split(
        X, y, test_size=0.20, random_state=42
    )  # dedicate 20% of samples to validation set
    return train_sentences, val_sentences, train_labels_plus_vul, val_labels_plus_vul


def make_predictions(model, val_sentences):
    """
    Makes predictions using the given model on the provided validation sentences.

    Args:
        model: The trained model used for making predictions.
        val_sentences: The validation sentences to make predictions on.

    Returns:
        y_pred: The predicted labels for the validation sentences.

    Example:
        >>> model = load_model(checkpoint_dir)
        >>> val_sentences = ["This is a positive sentence.", "This is a toxic sentence."]
        >>> y_pred = make_predictions(model, val_sentences)
        >>> print(y_pred)
    """
    y_pred = model.predict(val_sentences)
    y_pred[y_pred >= 0.5] = 1
    y_pred[y_pred < 0.5] = 0
    return y_pred


def evaluate_fairness(y_pred, val_labels_plus_vul):
    """
    Evaluate the fairness of a binary classification model.

    Args:
        y_pred (numpy.ndarray): Predicted labels of the model.
        val_labels_plus_vul (numpy.ndarray): Validation labels with vulnerability information.

    Returns:
        None

    Prints the fairness metrics based on the predicted labels and validation labels.

    Example:
        >>> y_pred = np.array([0, 1, 0, 1, 0])
        >>> val_labels_plus_vul = np.array([[0, 0], [1, 1], [0, 1], [1, 0], [0, 1]])

        >>> evaluate_fairness(y_pred, val_labels_plus_vul)
    """
    val_labels_df = pd.DataFrame(
        val_labels_plus_vul, columns=["toxicity", "vulnerability"]
    )
    val_labels_bld = BinaryLabelDataset(
        df=val_labels_df,
        label_names=["toxicity"],
        protected_attribute_names=["vulnerability"],
        favorable_label=0,
        unfavorable_label=1,
    )

    predictions_plus_vul = np.concatenate(
        [y_pred.astype(int), val_labels_plus_vul[:, 1].reshape(-1, 1)], axis=1
    )
    predictions_plus_vul_df = pd.DataFrame(
        predictions_plus_vul, columns=["toxicity", "vulnerability"]
    )
    predictions_bld = BinaryLabelDataset(
        df=predictions_plus_vul_df,
        label_names=["toxicity"],
        protected_attribute_names=["vulnerability"],
        favorable_label=0,
        unfavorable_label=1,
    )

    metric = ClassificationMetric(
        val_labels_bld,
        predictions_bld,
        privileged_groups=[{"vulnerability": 0}],
        unprivileged_groups=[{"vulnerability": 1}],
    )
    print_fairness_metrics(metric, val_labels_df, predictions_plus_vul_df)


def print_fairness_metrics(metric, val_labels_df, predictions_plus_vul_df):
    """
    Prints fairness metrics and interpretations based on the provided metric object, validation labels dataframe,
    and predictions plus vulnerability dataframe.

    Args:
        metric: The fairness metric object used to calculate fairness metrics.
        val_labels_df: The validation labels dataframe.
        predictions_plus_vul_df: The predictions plus vulnerability dataframe.

    Returns:
        None

    Example:
        >>> val_labels_df = pd.DataFrame(
            {
                "toxicity": [0, 1, 0, 1, 0],
                "vulnerability": [0, 1, 1, 0, 1]
            }
        )
        >>> predictions_plus_vul_df = pd.DataFrame(
            {
                "toxicity": [0, 1, 0, 1, 0],
                "vulnerability": [0, 1, 1, 0, 1]
            }
        )
        >>> metric = ClassificationMetric(
            val_labels_df,
            predictions_plus_vul_df,
            privileged_groups=[{"vulnerability": 0}],
            unprivileged_groups=[{"vulnerability": 1}],
        )
        >>> print_fairness_metrics(metric, val_labels_df, predictions_plus_vul_df)
    """

    disparate_impact = metric.disparate_impact()
    statistical_parity_difference = metric.statistical_parity_difference()
    equal_opportunity_difference = metric.equal_opportunity_difference()
    ent = between_group_generalized_entropy_error(
        val_labels_df, predictions_plus_vul_df, pos_label=0
    )
    treatment_equality = metric.num_false_negatives(
        privileged=False
    ) / metric.num_false_negatives(privileged=True) - metric.num_false_positives(
        privileged=False
    ) / metric.num_false_positives(
        privileged=True
    )

    # Print fairness metrics and interpretations
    print("Disparate Impact: ", disparate_impact)
    print("Statistical Parity Difference: ", statistical_parity_difference)
    print("Equal Opportunity Difference: ", equal_opportunity_difference)
    print("Generalized Entropy Error: ", ent)
    print("Treatment Equality: ", treatment_equality)

    if disparate_impact < 0.8:
        print(
            "The model exhibits potential bias as Disparate Impact is below the threshold (0.8)."
        )
    else:
        print(
            "The model demonstrates fairness as Disparate Impact is above the threshold (0.8)."
        )

    if abs(statistical_parity_difference) < 0.1:
        print(
            "Statistical Parity is nearly achieved, indicating fairness in impact between groups."
        )
    else:
        print(
            "Statistical Parity is not achieved, suggesting potential disparities in outcomes."
        )

    if metric.true_positive_rate() > 0.95:
        print(
            "The model has a very high True Positive Rate, EOD is not suitable to establish fairness."
        )
    else:
        if equal_opportunity_difference < 0.1:
            print(
                "Equal Opportunity is nearly achieved, indicating fairness in equal access to positive outcomes."
            )
        else:
            print(
                "Equal Opportunity is not achieved, suggesting potential disparities in equal access to positive outcomes."
            )
    if ent < 0.01:
        print(
            "Generalized Entropy is nearly achieved, indicating fairness in impact between groups."
        )
    else:
        print(
            "Generalized Entropy is not achieved, suggesting that equal privilege is not given to every individual."
        )
    if abs(treatment_equality) < 0.01:
        print(
            "Treatment Equality is nearly achieved, indicating fairness in impact between groups."
        )
    else:
        print("Equal treatment between all groups is not achieved.")


def main():
    """
    Main function to evaluate fairness.

    Loads a model from a checkpoint directory, reads a synthetic fairness dataset,
    preprocesses the data, splits it into validation data, makes predictions using the model,
    and evaluates the fairness of the predictions.

    Args:
        None

    Returns:
        None
    """
    model = load_model(checkpoint_dir)
    data_df = pd.read_csv("data/synthetic_fairness_dataset.csv")
    X, y = preprocess_data(data_df)
    (
        _,
        val_sentences,
        _,
        val_labels_plus_vul,
    ) = split_data(X, y)
    y_pred = make_predictions(model, val_sentences)
    evaluate_fairness(y_pred, val_labels_plus_vul)


if __name__ == "__main__":
    main()
