# Introduction to Machine Learning
Try to predict an outcome from past examples

There are 2 broad categories
- Supervised:
  - output is given (X->Y)
- Unsupervised
  - no output, just trying to learn structure (X)

There are 2 types of Supervised Learning:
- Classification
  - Trying to predict  a category or label
- Regression
  - predicting a real-valued number or vector


# Linear Regression

X = { x1, x2, x3, ....}
Y = { y1, y2, y3, ....}

Y = aX + b

Value of a

![a](http://latex.codecogs.com/gif.latex?a%20%3D%20%5Cfrac%7B%5Csum%20y_%7Bi%7Dx_%7Bi%7D%20-%20%5Cbar%7Bx%7D%5Csum%20x_%7Bi%7D%7D%7B%5Csum%20x_%7Bi%7D%5E%7B2%7D%20-%20%5Cbar%7Bx%7D%5Csum%7Bx_%7Bi%7D%7D%7D)

Value of b

![b-value](http://latex.codecogs.com/gif.latex?b%20%3D%20%5Cfrac%7B%5Cbar%7By%7D%5Csum%7Bx_%7Bi%7D%5E%7B2%7D%7D%20-%20%5Cbar%7Bx%7D%5Csum%20y_%7Bi%7Dx_%7Bi%7D%7D%7B%5Csum%20x_%7Bi%7D%5E%7B2%7D%20-%20%5Cbar%7Bx%7D%5Csum%7Bx_%7Bi%7D%7D%7D)

### To find the R-Squared value

**R-squared is a statistical measure of how close the data are to the fitted regression line.**

![r-square](http://latex.codecogs.com/gif.latex?R%5E%7B2%7D%20%3D%201%20-%20%5Cfrac%7B%5Csum%20%28%7By_%7Bi%7D-%5Chat%7By%7D%7D%29%5E2%7D%7B%5Csum%20%28y_%7Bi%7D%20-%20%5Cbar%20y%29%5E2%7D)
