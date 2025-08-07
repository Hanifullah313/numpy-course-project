import numpy as np
# fancy indexing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Accessing elements at specific indices
fancy_indices = arr[[0, 2], [1, 2]]  # Accessing elements at (0,1) and (2,2)
print("Elements at fancy indices (0,1) and (2,2):", fancy_indices)
# 1d array fancy indexing
arr1d = np.array([10, 20, 30, 40])  
# Accessing elements at specific indices in a 1D array
fancyindexes_1d = arr1d[[0, 3]]  # Accessing elements at indices 0 and 3
print("Elements at fancy indices 0 and 3 in 1D array:", fancyindexes_1d)