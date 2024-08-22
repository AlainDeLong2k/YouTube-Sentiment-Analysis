# Import necessary libraries and modules
import pickle
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

# Define constants for sentiment labels and model paths
NEGATIVE = 'Negative'  # Label for negative sentiment
POSITIVE = 'Positive'  # Label for positive sentiment
MAX_LEN = 300  # Maximum length of input sequences for the model
MODEL_PATH = 'sentiment_analysis_model.h5'  # Path to the saved sentiment analysis model
TOKENIZER_PATH = 'tokenizer.pickle'  # Path to the saved tokenizer

# Load the tokenizer from the specified path
with open(TOKENIZER_PATH, 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load the saved sentiment analysis model
model = load_model(MODEL_PATH)


def encode_texts(text_list):
    """
    Encodes a list of texts into padded sequences using the tokenizer.
    Parameters:
        text_list (list of str): A list of texts to encode.
    Returns:
        numpy.ndarray: Padded sequences ready for model input.
    """
    # Convert texts to sequences and pad them to a fixed length
    return pad_sequences(tokenizer.texts_to_sequences(text_list), maxlen=MAX_LEN)


def predict_sentiments(text_list):
    """
    Predicts sentiments for a list of texts using the loaded model.
    Parameters:
        text_list (list of str): A list of texts to analyze.
    Returns:
        list of str: A list of sentiment predictions ('Positive' or 'Negative').
    """
    # Encode the input texts for predicting sentiment
    encoded_inputs = encode_texts(text_list)
    predictions = model.predict(encoded_inputs)

    # If the prediction probability is below 0.5, assign a NEGATIVE sentiment; otherwise, assign a POSITIVE sentiment.
    sentiments = []  # Initialize an empty list to store sentiment results
    for predict in predictions:
        if predict < 0.5:
            sentiments.append(NEGATIVE)
        else:
            sentiments.append(POSITIVE)
    # Return the list of predicted sentiments.
    return sentiments
