import numpy as np
"""
What is broadcasting in numpy?
Broadcasting is a powerful mechanism that allows NumPy to work with arrays of different shapes when performing arithmetic operations.
It automatically expands the smaller array to match the shape of the larger array.
""" 
# Example of broadcasting with 1D and 2D arrays
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
result = arr_1d + arr_2d    # Broadcasting arr_1d to match arr_2d
print("1D array:\n", arr_1d)
print("2D array:\n", arr_2d)
print("Result of broadcasting:\n", result)
# Broadcasting example of discount
discount = 10  # 10% discount
# Applying discount to a 2D array of prices
price = np.array([[100, 200, 300], [400, 500, 600]])
final_price = price - (price * discount / 100)
print("Final price after discount:\n", final_price)