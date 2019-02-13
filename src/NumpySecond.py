""" numpy selecting array elements """

import numpy as np

a1 = np.arange(0, 10)
# print(a1[0], a1[1])

# select element in 2d array
# m = np.arange(0, 20).reshape(5, 4)
# print(m)
# print(m[1, 2])

# select all item in row 1
# print(m[1,])

# select all items in column 2
# print(m[:, 2])

''' Logical operation on arrays '''
a = np.arange(5)
# print((a < 2) | (a > 3))

# select items < 3
# print(a[a < 3])

# print(np.sum(a < 4))

# multiple array comparison
b1 = np.arange(0, 5)
b2 = np.arange(5, 0, -1)
# print(b1 < b2)

# 2d array comparison
c1 = np.arange(9).reshape(3, 3)
c2 = np.arange(9, 0, -1).reshape(3, 3)
print(c1 < c2)
