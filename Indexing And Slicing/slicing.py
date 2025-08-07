import numpy as np
#slicing a numpy array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Slicing the first two rows and first two columns
sliced_arr = arr[:2, :2]
print("Sliced array:\n", sliced_arr)
# slicing a 1D array
arr1d = np.array([10, 20, 30, 40, 50])
# Slicing the first three elements  
sliced_arr1d = arr1d[:3]
print("Sliced 1D array:", sliced_arr1d)
# Slicing with a step
sliced_arr_step = arr[::2, ::2]  # Every second row and column
print("Sliced array with step:\n", sliced_arr_step)
# Slicing with negative indices
sliced_arr_neg = arr[-2:, -2:]  # Last two rows and columns
print("Sliced array with negative indices:\n", sliced_arr_neg)
# Slicing with step on 1d array
sliced_arr1d_step = arr1d[::-1]  # Reverse the array
print("Sliced 1D array with step:", sliced_arr1d_step)