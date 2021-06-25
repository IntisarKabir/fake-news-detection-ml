










#######     svm     ######


from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig
# define a matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
# calculate the mean of each column
M = mean(A.T, axis=1)
print(M)
# center columns by subtracting column means
C = A - M
print(C)
# calculate covariance matrix of centered matrix
V = cov(C.T)
print(V)
# eigendecomposition of covariance matrix
values, vectors = eig(V)
print(vectors)
print(values)
# project data
P = vectors.T.dot(C.T)
print(P.T)



A - mean(A.T, axis=1)


cov(C.T)



###############     amplitude moDem.ipynb             ##############


conda install am_analysis


import numpy as np
import matplotlib.pyplot as plt
from am_analysis import am_analysis as ama


import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st









