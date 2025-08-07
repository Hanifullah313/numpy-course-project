import numpy as np 
"""
delete :
Delete elements from an array at specified indices.
"""
# Deleting elements from an array
arr = np.array([1, 2, 3, 4, 5])
deleted_arr = np.delete(arr, [1])  # Delete elements at indices 1 
print("Original array:\n", arr)
print("Array after deletion:\n", deleted_arr)

# 2D array deletion
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
deleted_2d = np.delete(arr_2d, 0, axis=0)  # Delete the first row
print("Original 2D array:\n", arr_2d)
print("2D array after deletion:\n", deleted_2d)