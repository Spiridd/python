from urllib.request import urlopen
import numpy as np
from numpy.linalg import inv


filename = "https://stepic.org/media/attachments/lesson/16462/boston_houses.csv"
f = urlopen(filename)
matrix = np.loadtxt(f, skiprows=1, delimiter=",")
Y = matrix[:, 0]
X = np.hstack((np.ones((matrix.shape[0], 1)), matrix[:, 1:]))
bettas = inv(X.T.dot(X)).dot(X.T).dot(Y)
[print(betta, end=" ") for betta in bettas]
