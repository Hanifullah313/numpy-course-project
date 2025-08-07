import numpy as np
"""
contatenate ?
Concatenate two or more arrays along a specified axis.
axis 0 concatenates along rows
axis 1 concatenates along columns
"""
# Concatenating 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated_1d = np.concatenate((arr1, arr2))
print("Concatenated 1D array:\n", concatenated_1d)

# Concatenating 2D arrays
arr_2d_1 = np.array([[1, 2, 3], [4, 5, 6]])
arr_2d_2 = np.array([[7, 8, 9]])
concatenated_2d = np.concatenate((arr_2d_1, arr_2d_2), axis=0)
print("Concatenated 2D array (axis 0):\n", concatenated_2d)