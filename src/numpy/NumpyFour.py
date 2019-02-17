import numpy as np

a = np.arange(0, 9)
# print(a)

m = a.reshape(3, 3)
# print(m)

# print(m.reshape(9))
# print(m.ravel())

# @doc .reshape() and .ravel() do not change shape of original array but change contents in the original array

# reshaped into array
reshaped = m.reshape(np.size(m))

# ravel into array
raveled = m.ravel()

reshaped[2] = 1000
raveled[5] = 2000

# print(m)

# @doc .flatten is like ravel, but does not change original data
m2 = np.arange(0, 9).reshape(3, 3)
flattened = m2.flatten()
flattened[0] = 1000
# print(flattened)

# print(m2)
# print(m2.T)

''' Combining array '''
a = np.arange(9).reshape(3, 3)
b = (a + 1) * 10
# print(b)

# print(np.concatenate((a, b), axis=1))  # similar to np.hstack((a,b))
# print(np.concatenate((a, b), axis=0))  # similar to np.vstack((a,b))
print(np.dstack((a, b)))
