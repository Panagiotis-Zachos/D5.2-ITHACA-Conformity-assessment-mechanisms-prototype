import pandas as pd
import numpy as np
import random


def load_dataset(file_path):
    """
    Load the dataset from a CSV file.

    Parameters:
    - file_path: str, the path to the CSV file.

    Returns:
    - df: DataFrame, the loaded dataset.
    """
    df = pd.read_csv(file_path)
    return df


def assign_vulnerability(df, prob_vul=0.2, prob_unfair=0.7):
    """
    Assign vulnerability status to rows in the dataset based on given probabilities.

    Parameters:
    - df: DataFrame, the dataset to modify.
    - prob_vul: float, the percentage of the population that is vulnerable.
    - prob_unfair: float, the percentage of the vulnerable population that is unfairly treated.

    Returns:
    - df: DataFrame, the dataset with assigned vulnerability statuses.
    """

    df["vulnerability"] = 0
    num_rows = len(df)
    tox_idxs = df[df["Toxicity"] == 1].index.tolist()
    vul_idxs1 = random.sample(
        tox_idxs, np.ceil(prob_unfair * prob_vul * num_rows).astype(int)
    )

    nontox_idxs = df[df["Toxicity"] == 0].index.tolist()
    vul_idxs2 = random.sample(
        nontox_idxs, np.ceil((1 - prob_unfair) * prob_vul * num_rows).astype(int)
    )

    vul_idxs = vul_idxs1 + vul_idxs2
    df.loc[vul_idxs, "vulnerability"] = 1
    return df


def print_vulnerability_stats(df):
    """
    Print statistics about the vulnerability distribution in the dataset.

    Parameters:
    - df: DataFrame, the dataset to analyze.
    """
    num_rows = len(df)
    print(
        "Percentage of vulnerable people: {:.2f}%".format(
            100 * len(df[df["vulnerability"] == 1].index.tolist()) / num_rows
        )
    )

    print(
        "Percentage of vulnerable people treated with bias: {:.2f}%".format(
            100
            * len(df[(df["vulnerability"] == 1) & (df["Toxicity"] == 1)])
            / len(df[df["vulnerability"] == 1].index.tolist())
        )
    )


def save_dataset(df, file_path):
    """
    Save the DataFrame to a CSV file.

    Parameters:
    - df: DataFrame, the dataset to save.
    - file_path: str, the path to save the CSV file.
    """
    df.to_csv(file_path, index=False)


# Example usage
if __name__ == "__main__":
    df = load_dataset("data/FinalBalancedDataset.csv")
    df = assign_vulnerability(df)
    print_vulnerability_stats(df)
    save_dataset(df, "data/synthetic_fairness_dataset.csv")
