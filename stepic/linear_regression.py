import numpy as np
from numpy.linalg import inv


distances = [10, 7, 12]
speeds = [60, 50, 75]

d_avg = sum(distances)/len(distances)
s_avg = sum(speeds)/len(speeds)

betta1 = sum([s*(d_avg-d) for s, d in zip(speeds, distances)])/sum([s*(s_avg-s) for s in speeds])
betta0 = d_avg - betta1*s_avg
print(betta0, betta1)

# another way
Y = np.array([10, 7, 12])
X = np.ones((3, 2))
X[:, 1] = [60, 50, 75]
betta = inv(X.T.dot(X)).dot(X.T).dot(Y)
print(betta)
