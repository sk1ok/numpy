"""
We create a 1D NumPy array arr_1d with values [1, 2, 3, 4, 5].
We create a 2D NumPy array arr_2d with values [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
We access elements in both arrays using indexing.
We perform mathematical operations on the arrays, squaring each element in arr_1d and calculating the sum along columns in arr_2d
"""

import numpy as np

# Creating a 1D NumPy array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D NumPy Array:")
print(arr_1d)

# Creating a 2D NumPy array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D NumPy Array:")
print(arr_2d)

# Accessing elements of a NumPy array
element_1d = arr_1d[2]
element_2d = arr_2d[1, 2]
print("\nAccessing Elements:")
print(f"Element at index 2 in arr_1d: {element_1d}")
print(f"Element at row 1, column 2 in arr_2d: {element_2d}")

# Performing mathematical operations on a NumPy array
arr_squared = arr_1d**2
arr_sum = np.sum(arr_2d, axis=0)  # Sum along columns
print("\nMathematical Operations:")
print(f"Square each element in arr_1d: {arr_squared}")
print(f"Sum of elements along columns in arr_2d: {arr_sum}")
