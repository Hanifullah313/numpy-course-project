import numpy as np
# basic mathematical operations on numpy arrays
arr1 = np.array([1, 2, 3])  
arr2 = np.array([4, 5, 6])
arr_sum = arr1 + arr2
arr_diff = arr1 - arr2
arr_product = arr1 * arr2
arr_quotient = arr1 / arr2
print("Sum:", arr_sum)
print("Difference:", arr_diff)  
print("Product:", arr_product)
print("Quotient:", arr_quotient)
arr_square = arr1 ** 2
print("Square of arr1:", arr_square)
arr_sqrt = np.sqrt(arr1)
print("Square root of arr1:", arr_sqrt)
arr_exp = np.exp(arr1)
print("Exponential of arr1:", arr_exp)
arr_log = np.log(arr1)
print("Logarithm of arr1:", arr_log)
arr_max = np.max(arr1)
arr_min = np.min(arr1)
print("Maximum of arr1:", arr_max)
print("Minimum of arr1:", arr_min)
print("adding two to arr1:", arr1 + 2)
