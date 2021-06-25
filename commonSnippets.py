




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('fivethirtyeight')
import seaborn as sns; sns.set()


from datetime import datetime



import warnings
warnings.filterwarnings("ignore")






from google.colab import files
uploaded = files.upload()



from pandas import Series


import keras
from keras.layers import SimpleRNN, Embedding, Dense, LSTM,  Embedding, Dropout
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle







