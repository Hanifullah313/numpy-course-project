import numpy as np
"""
splitting:
Split an array into multiple sub-arrays along a specified axis.
hsplit is used to split arrays horizontally (along columns),
vsplit is used to split arrays vertically (along rows).
split is a more general function that can split arrays along any axis.
"""
# Splitting a 1D array
arr_1d = np.array([1, 2, 3, 4, 5, 6])
split_1d = np.split(arr_1d, 3)
print("Split 1D array:\n", split_1d)
# Splitting a 2D array horizontally
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
h_split_2d = np.hsplit(arr_2d, 3)  # Split into 3 equal parts along columns
print("Horizontally split 2D array:\n", h_split_2d) 
