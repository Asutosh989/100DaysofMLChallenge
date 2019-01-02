import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

for line in open('./data/data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

X = np.array(X)
Y = np.array(Y)

# plt.scatter(X,Y)
# plt.show()

# applying the equations to calculate a and b
denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum()) / denominator
b = (Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) / denominator

# Calculate the predicted Y
Y_predicted = a*X +b

# plot the result
plt.scatter(X, Y)
plt.plot(X, Y_predicted)
plt.show()

# calculate r-squared
d1 = Y - Y_predicted
d2 = Y - Y.mean()
r2 = 1 - (d1.dot(d1) / d2.dot(d2))
print("R-squared value is ", r2)
