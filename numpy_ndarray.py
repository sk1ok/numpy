"""
We use numpy.ndarray to create a 1D array (arr_1d) with a specified shape, data type (dtype), and buffer (existing array).
We use numpy.ndarray to create a 2D array (arr_2d) with a specified shape, data type, and buffer.
We access elements in both arrays using indexing.
"""

import numpy as np

# Using numpy.ndarray to create a 1D array
arr_1d = np.ndarray(shape=(5,), dtype=int, buffer=np.array([1, 2, 3, 4, 5]))
print("1D NumPy Array:")
print(arr_1d)

# Using numpy.ndarray to create a 2D array
arr_2d = np.ndarray(shape=(3, 3), dtype=float, buffer=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print("\n2D NumPy Array:")
print(arr_2d)

# Accessing elements of a NumPy array
element_1d = arr_1d[2]
element_2d = arr_2d[1, 2]
print("\nAccessing Elements:")
print(f"Element at index 2 in arr_1d: {element_1d}")
print(f"Element at row 1, column 2 in arr_2d: {element_2d}")