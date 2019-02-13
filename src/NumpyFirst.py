# basic numpy array creation

import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
# print(a1)
# print(np.size(a1))

# shorthand to repeat sequence 10 times
a3 = np.array([0] * 10)
# print(a3)

# convert python range to numpy array
# print(np.array(range(10)))

# create numpy array of 10 0's
# print(np.zeros(10, dtype=int))

# make a range starting at 0 to 10
# print(np.arange(1, 10))

# increment by 2
# print(np.arange(0, 10, 2))

# count down
# print(np.arange(10, 0, -1))

# linspace: similar to arange but generates an array of specific number of items between specified start and stop values
# print(np.linspace(0, 10, 11, dtype=int))

# multiply numpy array by 2
b1 = np.arange(0, 10)
# print(b1 * 2)

b2 = np.arange(10, 20)
# print(b1 + b2)

# create 2-dim array
print(np.array([[1, 2], [3, 4]]))

# create a 1x20 array and reshape to a  5x4 2d-array
m = np.arange(0, 20).reshape(5, 4)
print(m)
print(np.size(m))

# determine the number of rows in 2d array, we can pass 0 as another parameter
print(np.size(m, 0))

# determine the number of columns in 2d array, we can pass 1 as another params
print(np.size(m, 1))
