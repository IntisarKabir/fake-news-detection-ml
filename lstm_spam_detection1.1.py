

import pandas as pd

dataset_url = "https://raw.githubusercontent.com/IntisarKabir/ml-datasets/main/commonDatasets/spam.csv"
df = pd.read_csv(dataset_url , encoding='latin-1')
print(df.shape)
df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1, inplace=True)
df.columns = ["SpamHam","Tweet"]
print(df.shape)


!pip install contractions #pip 
import contractions


import numpy as np
import re
import collections

import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('dark_background')



import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import warnings
warnings.simplefilter(action='ignore', category=Warning)



import keras
from keras.layers import Dense, Embedding, LSTM, Dropout
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle



sns.countplot(df["SpamHam"])



def word_count_plot(data):
     # finding words along with count
     word_counter = collections.Counter([word for sentence in data for word in sentence.split()])
     most_count = word_counter.most_common(30) # 30 most common words
     # sorted data frame
     most_count = pd.DataFrame(most_count, columns=["Word", "Count"]).sort_values(by="Count")
     most_count.plot.barh(x = "Word", y = "Count", color="green", figsize=(10, 15))
word_count_plot(data["Tweet"])










