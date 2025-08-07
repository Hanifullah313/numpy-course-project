"""
Reshaping and modifying arrays in NumPy
if the dimensions of the array are not compatible with the new shape, an error will be raised.
This code snippet demonstrates how to reshape a NumPy array.
they do not make copy but display the view of the original array.
"""
import numpy as np  

# Reshaping an array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
reshaped_arr = arr.reshape(1, 9)  # Reshape to 1 row and 9 columns
print("Original array:\n", arr)     
print("Reshaped array:\n", reshaped_arr)

#now from 1d to 2d
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped_2d = arr_1d.reshape(3, 3)  # Reshape to 3 rows and 3 columns
print("1D array:\n", arr_1d)
print("Reshaped 2D array:\n", reshaped_2d)
