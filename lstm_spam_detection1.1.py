

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



