import numpy as np
# This script creates a NumPy array and prints it
arr = np.array([1, 2, 3, 4, 5])
print("Array created using np.array:")
print(arr)
# The array is a simple one-dimensional array with integers
# It can be used for various numerical operations in Python

#array with default dtype
arr1 = np.zeros(5)
print("Array created using np.zeros with default dtype:")
print(arr1)


#array with default 2d
arr1 = np.zeros((2, 5 ))
print("Array created using np.zeros with shape (2, 5):")
print(arr1)


#array with default 3d
arr1 = np.zeros((2, 5, 3))
print("Array created using np.zeros with shape (2, 5, 3):")
print(arr1)

#array with default ones
arr2 = np.ones(5)
print("Array created using np.ones with default dtype:")
print(arr2)

#array with default values "full"
arr2 = np.full((5, 7), 8)
print("Array created using np.full with default values  :")
print(arr2)


