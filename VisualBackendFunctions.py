'''
The provided Python script is used for cleaning and processing tweets from a dataset. Here's a step-by-step explanation:

The script begins by importing necessary libraries such as numpy, pandas, re (for regular expressions), emoji (for handling emojis), and nltk (Natural Language Toolkit, for text processing).

The cleaner(tweet) function is defined to clean a single tweet. It performs the following operations:

Converts the tweet to lowercase.
Removes @mentions and URLs.
Removes emojis.
Removes all characters that are not alphabets.
Removes stopwords (commonly used words like 'is', 'the', 'and', etc. that do not carry much meaning).
The get_words(f) function is a generator function that cleans each line in the input f using the cleaner function.

The returnTweets() function is defined to return the variable x_pc.

A set of English words and a list of English stopwords are loaded from the nltk corpus.

A pandas DataFrame is created from a CSV file named "synthetic_fairness_dataset.csv" located in the "data" directory.

The "tweet" column from the DataFrame is extracted, cleaned using the get_words function, and stored in the variable X.

The variable x_pc is defined as a subset of X containing specific indices.

Finally, the cleaned tweets in X are printed to the console.

Please note that there are some commented lines in the script which are not currently in use but could be used for additional processing, such as removing URLs, shuffling the DataFrame, and removing hashtags.
'''

import numpy as np
import pandas as pd
import re
import emoji
import nltk
from nltk.corpus import stopwords

def cleaner(tweet):
    tweet = tweet.lower()
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.EMOJI_DATA) #Remove Emojis
    # tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    tweet = re.sub("[^A-Za-z ]+", '', tweet)
    # tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) \
    #      if w.lower() in words or not w.isalpha())
    tweet = ' '.join([word for word in tweet.split() if word not in cachedStopWords])

    return tweet

def get_words(f):
    for line in f:
        yield cleaner(line)

def returnTweets():
    # return X[1:]
    return x_pc

words = set(nltk.corpus.words.words())
cachedStopWords = stopwords.words("english")
data_df = pd.read_csv("data/synthetic_fairness_dataset.csv")

# Shuffle training dataframe
# data_df = data_df.sample(
#     frac=1,
#     random_state=42
# )  # shuffle with random_state=42 for reproducibility

# X = [re.sub("http://\S+|https://\S+", "", text) for text in data_df["tweet"]]
X = np.array(data_df["tweet"])
X = list(get_words(X))
x_pc = [X[1], X[3], X[4], X[6], X[20], X[10], X[14], X[16], X[101], X[100], X[17], X[21], X[24], X[36], X[151], X[58], X[62], X[156], X[41], X[53]]


# Select Tweets
print(X)