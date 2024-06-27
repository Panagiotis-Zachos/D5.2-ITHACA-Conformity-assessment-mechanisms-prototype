import tensorflow as tf
from tensorflow.keras import layers
import pickle
import tensorflow_privacy
import numpy as np
from tensorflow_privacy.privacy.privacy_tests.membership_inference_attack import (
    membership_inference_attack as mia,
    # privacy_report,
)
from tensorflow_privacy.privacy.privacy_tests.membership_inference_attack.data_structures import (
    AttackInputData,
    PrivacyReportMetadata,
    AttackType,
    SlicingSpec,
)


def create_model(train_sentences=None):
    max_vocab_length = 10000
    max_length = 15  # max length our sequences will be (e.g. how many words from a Tweet does our model see?)
    text_vectorizer = layers.TextVectorization(
        max_tokens=max_vocab_length,  # how many words in the vocabulary (all of the different words in your text)
        standardize="lower_and_strip_punctuation",  # how to process text
        split="whitespace",  # how to split tokens
        ngrams=None,  # create groups of n-words?
        output_mode="int",  # how to map tokens to numbers
        output_sequence_length=max_length,
    )  # how long should the output sequence of tokens be?
    # pad_to_max_tokens=True) # Not valid if using max_tokens=None

    if train_sentences is not None:  # Fit and save the text vectorizer during training
        text_vectorizer.adapt(train_sentences)
        pickle.dump(
            {
                "config": text_vectorizer.get_config(),
                "weights": text_vectorizer.get_weights(),
            },
            open("./models/tv_layer.pkl", "wb"),
        )
    else:  # Load the text vectorizer from disk
        from_disk = pickle.load(open("./models/tv_layer.pkl", "rb"))
        text_vectorizer = layers.TextVectorization.from_config(from_disk["config"])

        # Call `adapt` with some dummy data (BUG in Keras)
        text_vectorizer.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))
        text_vectorizer.set_weights(from_disk["weights"])

    embedding = layers.Embedding(
        input_dim=max_vocab_length,  # set input shape
        output_dim=128,  # set size of embedding vector
        embeddings_initializer="uniform",  # default, intialize randomly
        input_length=max_length,  # how long is each input embedding
        name="embedding_1",
    )

    inputs = layers.Input(shape=(1,), dtype="string")
    x = text_vectorizer(inputs)
    x = embedding(x)
    x = layers.GlobalAveragePooling1D()(x)

    outputs = layers.Dense(1, activation="sigmoid")(x)

    model = tf.keras.Model(inputs, outputs, name="model_dense")
    model.compile(
        loss="binary_crossentropy",
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        metrics=["accuracy"],
    )

    return model


def create_dp_model(train_sentences=None):
    """
    This Python function, create_dp_model(train_sentences=None), is used to create a differentially private (DP) model for text classification tasks. It uses TensorFlow and TensorFlow Privacy libraries. The function is divided into several sections:

    Text Vectorization: The function creates a TextVectorization layer from TensorFlow's Keras API. This layer transforms strings into a list of integer indices representing words. The parameters for this layer include the maximum vocabulary length, the standardization method, the token split method, the output mode, and the output sequence length.

    Vectorizer Training/Loading: If train_sentences are provided, the function fits the TextVectorization layer to the training data and saves the vectorizer's configuration and weights to disk. If train_sentences are not provided, the function loads the vectorizer's configuration and weights from disk.

    Embedding Layer: The function creates an Embedding layer, which transforms integer indices into dense vectors of fixed size. The parameters for this layer include the input dimension, the output dimension, the embeddings initializer, the input length, and the layer name.

    Model Architecture: The function defines the architecture of the DP model. The model takes a string input, applies the TextVectorization layer, applies the Embedding layer, applies a GlobalAveragePooling1D layer, and finally applies a Dense layer with a sigmoid activation function.

    Differential Privacy Optimizer: The function creates a DPKerasAdamOptimizer from the TensorFlow Privacy library. This optimizer implements the Adam algorithm with differential privacy. The parameters for this optimizer include the L2 norm clip, the noise multiplier, the number of microbatches, and the learning rate.

    Model Compilation: The function compiles the model with the binary cross-entropy loss function, the DP optimizer, and accuracy as the metric.

    Return: The function returns the compiled model.

    This function is used to create a model that can be trained on text data while preserving the privacy of the data. The model can be used for binary text classification tasks.

    Parameters:
        train_sentences (list, optional): A list of sentences used for training the TextVectorization layer. Defaults to None.

    Returns:
        tf.keras.Model: The compiled differentially private model for text classification.
    """
    # Function code here
    pass


class PrivacyMetricsCallback(tf.keras.callbacks.Callback):
    """
    Callback class for computing privacy metrics during training.

    Args:
        epochs_per_report (int): Number of epochs between privacy reports.
        x_train (numpy.ndarray): Training data.
        x_test (numpy.ndarray): Test data.
        y_train_indices (numpy.ndarray): Training labels.
        y_test_indices (numpy.ndarray): Test labels.
        batch_size (int): Batch size for predictions.
        model_name (str): Name of the model.

    Attributes:
        x_train (numpy.ndarray): Training data.
        x_test (numpy.ndarray): Test data.
        y_train_indices (numpy.ndarray): Training labels.
        y_test_indices (numpy.ndarray): Test labels.
        batch_size (int): Batch size for predictions.
        epochs_per_report (int): Number of epochs between privacy reports.
        model_name (str): Name of the model.
        attack_results (list): List to store the results of privacy attacks.

    The PrivacyMetricsCallback class is a callback used for computing privacy metrics during training. It takes several arguments in its constructor, including epochs_per_report, x_train, x_test, y_train_indices, y_test_indices, batch_size, and model_name. These arguments are used to initialize the attributes of the class.

    The PrivacyMetricsCallback class has a method called on_epoch_end which is called at the end of each epoch during training. Inside this method, there is a check to determine if the current epoch is a multiple of epochs_per_report. If it is, a privacy report is generated.

    To generate the privacy report, the method first uses the model attribute (which is assumed to be an instance of a TensorFlow Keras model) to make predictions on the training and test data (x_train and x_test). The predictions are stored in prob_train and prob_test respectively.

    Next, the method creates an instance of the PrivacyReportMetadata class, which is used to store metadata about the evaluated model. The metadata includes the training and test accuracy, the epoch number, and the model variant label (which is set to the model_name argument).

    The method then calls the run_attacks function, passing in the necessary inputs such as the attack input data, the slicing specification, the attack types, and the privacy report metadata. The run_attacks function is responsible for running membership inference attacks on the model.

    The results of the attacks are stored in the attack_results attribute of the PrivacyMetricsCallback class. These results can be accessed and analyzed after training is complete.

    Overall, the PrivacyMetricsCallback class provides a convenient way to compute privacy metrics during training by generating privacy reports and running membership inference attacks on the model.
    """

    def __init__(
        self,
        epochs_per_report,
        x_train,
        x_test,
        y_train_indices,
        y_test_indices,
        batch_size,
        model_name,
    ):
        self.x_train = x_train
        self.x_test = x_test
        self.y_train_indices = y_train_indices
        self.y_test_indices = y_test_indices
        self.batch_size = batch_size
        self.epochs_per_report = epochs_per_report
        self.model_name = model_name
        self.attack_results = []

    def on_epoch_end(self, epoch, logs=None):
        epoch = epoch + 1

        if epoch % self.epochs_per_report != 0:
            return

        print(f"\nRunning privacy report for epoch: {epoch}\n")
        prob_train = self.model.predict(self.x_train, batch_size=self.batch_size)
        prob_test = self.model.predict(self.x_test, batch_size=self.batch_size)

        # prob_train = special.softmax(logits_train, axis=1)
        # prob_test = special.softmax(logits_test, axis=1)

        # Add metadata to generate a privacy report.
        privacy_report_metadata = PrivacyReportMetadata(
            # Show the validation accuracy on the plot
            # It's what you send to train_accuracy that gets plotted.
            accuracy_train=logs["val_accuracy"],
            accuracy_test=logs["val_accuracy"],
            epoch_num=epoch,
            model_variant_label=self.model_name,
        )
        attack_results = mia.run_attacks(
            AttackInputData(
                labels_train=np.squeeze(self.y_train_indices[:]),
                labels_test=self.y_test_indices[:],
                probs_train=prob_train,
                probs_test=prob_test,
            ),
            SlicingSpec(entire_dataset=True, by_class=True),
            attack_types=(
                AttackType.LOGISTIC_REGRESSION,
                # AttackType.MULTI_LAYERED_PERCEPTRON,
                # AttackType.RANDOM_FOREST,
                AttackType.K_NEAREST_NEIGHBORS,
                AttackType.THRESHOLD_ATTACK,
                # AttackType.THRESHOLD_ENTROPY_ATTACK,
            ),
            privacy_report_metadata=privacy_report_metadata,
        )

        self.attack_results.append(attack_results)
