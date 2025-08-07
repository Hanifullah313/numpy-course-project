import numpy as np
"""
what is vectorization in numpy?
Vectorization is the process of performing operations on entire arrays rather than element by element, which leads to more efficient computations.
difference between vectorization and broadcasting?
Vectorization refers to the ability to perform operations on entire arrays at once, while broadcasting allows for operations between arrays of different shapes by automatically expanding the smaller array.
"""
# Example of vectorization with a simple operation
arr = np.array([1, 2, 3, 4, 5])
arr = arr * 2 # Vectorized operation to multiply each element by 2
print("Vectorized array:\n", arr)
# Example of vectorization with a mathematical function
arr = np.array([1, 2, 3, 4, 5])
arr = np.sin(arr)  # Vectorized operation to apply the sine function to each element
print("Vectorized array with sine function:\n", arr)