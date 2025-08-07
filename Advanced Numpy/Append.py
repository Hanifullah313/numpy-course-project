import numpy as np
"""
what is append in numpy?
Append elements to the end of an array.
"""
# Appending elements to an array
arr = np.array([1, 2, 3, 4, 5])
appended_arr = np.append(arr, [6, 7])  # Append 6 and 7 to the end of the array
print("Original array:\n", arr)
print("Array after appending:\n", appended_arr)
# 2D array appending
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
appended_2d = np.append(arr_2d, [[7, 8, 9]], axis=0)  # Append a new row at the end
print("Original 2D array:\n", arr_2d)
print("2D array after appending:\n", appended_2d)