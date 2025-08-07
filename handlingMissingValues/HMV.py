import numpy as np
"""

Handling Missing Values
========================

In real-world data, missing values are common. NumPy provides several ways to handle missing values in arrays.

1. Identifying Missing Values
   You can use the `np.isnan()` function to identify missing values (NaN) in an array.

2. Removing Missing Values
   You can remove missing values from an array using boolean indexing.

3. Replacing Missing Values
   You can replace missing values with a specific value using the `np.nan_to_num()` function or by using boolean indexing.

three common functions to handle missing values:
1. `np.isnan()`: Identify missing values.
2. `np.nan_to_num()`: Replace missing values with a specified value.
3. Boolean indexing: Remove or replace missing values based on conditions.
infinity values can be handled similarly to NaN values using `np.isinf()`.
"""
# using np.nan to represent missing values
arr = np.array([1, 2, np.nan, 4, 5])
# Identifying missing values
missing_mask = np.isnan(arr)
print("Missing values mask:\n", missing_mask)
# Removing missing values
arr_cleaned = arr[~missing_mask]
print("Array after removing missing values:\n", arr_cleaned)
# Replacing missing values with zero
arr_filled = np.nan_to_num(arr, nan=0)
print("Array after replacing missing values with zero:\n", arr_filled)



# Handling infinity values
arr_inf = np.array([1, 2, np.inf, -np.inf, 5])
# Identifying infinity values
inf_mask = np.isinf(arr_inf)
print("Infinity values mask:\n", inf_mask)
# Removing infinity values
arr_inf_cleaned = arr_inf[~inf_mask]
print("Array after removing infinity values:\n", arr_inf_cleaned)
# Replacing infinity values with zero
arr_inf_filled = np.where(inf_mask, 0, arr_inf)
print("Array after replacing infinity values with 0:\n", arr_inf_filled)



