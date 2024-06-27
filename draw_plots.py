import matplotlib.pyplot as plt

from tensorflow_privacy.privacy.privacy_tests.membership_inference_attack import (
    privacy_report,
)
from tensorflow_privacy.privacy.privacy_tests.membership_inference_attack.data_structures import (
    PrivacyMetric,
    AttackResultsCollection,
)


if __name__ == '__main__':
    privacy_metrics = (
    PrivacyMetric.AUC,  # https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
    PrivacyMetric.ATTACKER_ADVANTAGE,
    PrivacyMetric.PPV,
)  # AUC, ATTACKER_ADVANTAGE, PPV, EPSILON_LOWER_BOUND
    # epoch_plot = privacy_report.plot_by_epochs(results, privacy_metrics=privacy_metrics)

    # plt.show()
    results_private = AttackResultsCollection.load("results\dp_model")
    all_results_private_df = privacy_report._calculate_combined_df_with_metadata(results_private.attack_results_list)

    results_normal = AttackResultsCollection.load("results\\normal_model")
    all_results_normal_df = privacy_report._calculate_combined_df_with_metadata(results_normal.attack_results_list)

    legend_labels = all_results_private_df['legend label'].unique() # Attack names
    legend_labels = [legend_labels[-1]]
    fig, axes = plt.subplots(len(legend_labels), len(privacy_metrics), figsize=(11, 4), sharex=True)
    x_axis_metric='Epoch'

    for i, privacy_metric in enumerate(privacy_metrics):
        for j, legend_label in enumerate(legend_labels):
            single_label_results = all_results_private_df.loc[all_results_private_df['legend label'] == legend_label]
            sorted_label_results = single_label_results.sort_values(x_axis_metric)
            axes[i].plot(sorted_label_results[x_axis_metric], sorted_label_results[str(privacy_metric)])
            axes[i].set_xlabel(x_axis_metric)

            single_label_results = all_results_normal_df.loc[all_results_normal_df['legend label'] == legend_label]
            sorted_label_results = single_label_results.sort_values(x_axis_metric)
            axes[i].plot(sorted_label_results[x_axis_metric], sorted_label_results[str(privacy_metric)])
            axes[i].set_xlabel(x_axis_metric)


    axes[0].set_ylabel('{}'.format(privacy_metrics[0]))
    axes[1].set_ylabel('{}'.format(privacy_metrics[1]))
    axes[2].set_ylabel('{}'.format(privacy_metrics[2]))
    axes[1].set_title('{}'.format('Threshold Attack'))
    axes[2].legend(['Differentially Private Model', 'Baseline Model'], loc='upper right')
    plt.tight_layout()  # Leave space for suptitle.

    plt.show()
    plt.close('all')