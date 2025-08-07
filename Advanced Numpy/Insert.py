import numpy as np  
""" insert elements into an array at specified indices """
# Inserting elements into an array
arr = np.array([1, 2, 3, 4, 5])         
inserted_arr = np.insert(arr, 4, [6, 7])  # Insert 6 and 7 at index 4
# The original array remains unchanged, and a new array is returned
print("Original array:\n", arr) 
print("Array after insertion:\n", inserted_arr)

# 2d array insertion
arr_2d = np.array([[1, 2, 3], [4,   5, 6]])
inserted_2d = np.insert(arr_2d, 1, [7, 8, 9], axis=0)  # Insert a new row at index 1
print("Original 2D array:\n", arr_2d)   
print("2D array after insertion:\n", inserted_2d)