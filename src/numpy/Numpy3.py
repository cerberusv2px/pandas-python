# Slicing array

import numpy as np

a1 = np.arange(1, 10)
# print(a1)
# print('------------------------------')

# select from position 3 up to 8th element
# print(a1[3:8])

# select every other items
# print(a1[::2])

# select items in reverse order
# print(a1[::-1])

# selecting element in reverse does not include element specified in the second component of the slice.
# i.e there is no 1 printed
# print(a1[9:0:-1])

# select all items from position 5 onwards
# print(a1[5:])

# select items in first 5 position
# print(a1[:5])

m = np.arange(0, 20).reshape(5, 4)
print(m)
print('------------------------------')

# gets items in column position 1, all rows
# print(m[:, 1])

# get items in column position 1:3, all rows
# print(m[:, 1:3])

# get items in row position 3 up to but not including 5, all columns
# print(m[3:5, :])

# selecting specific row or columns
# print(m[[1, 3, 4], :])


''' Reshaping array '''


