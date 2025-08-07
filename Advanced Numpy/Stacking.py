import numpy as np
"""
what is stacking in numpy?
Stacking is the process of joining multiple arrays along a new axis.
vstack and hstack are used to stack arrays vertically and horizontally, respectively.
"""
# Stacking 1D arrays through vstack and hstack
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
stacked_1d_v = np.vstack((arr1, arr2))
stacked_1d_h = np.hstack((arr1, arr2))
print("Stacked 1D array (vstack):\n", stacked_1d_v)
print("Stacked 1D array (hstack):\n", stacked_1d_h)
# Stacking 2D arrays 
"""arr_2d_1 = np.array([[1, 2, 3], [4, 5, 6]])
arr_2d_2 = np.array([[7, 8, 9]])
stacked_2d_v = np.stack((arr_2d_1, arr_2d_2), )
stacked_2d_h = np.stack((arr_2d_1, arr_2d_2), )
print("Stacked 2D array (vstack):\n", stacked_2d_v)
print("Stacked 2D array (hstack):\n", stacked_2d_h)"""