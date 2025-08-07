import numpy as np
"""
.ravel ==> view
.flattern ==> copy 
"""
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Flattening an array
flattened_arr = arr.flatten()  # Returns a copy of the array collapsed into one dimension
print("Original array:\n", arr)
print("Flattened array:\n", flattened_arr)
# ravel 
raveled_arr = arr.ravel()  # Returns a flattened view of the array
print("Raveled array:\n", raveled_arr)