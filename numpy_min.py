"""
We create a 2D NumPy array (arr_2d) with some values.
We use np.min(arr_2d) to find the minimum value in the entire array.
We use np.min(arr_2d, axis=0) to find the minimum values along each column.
We use np.min(arr_2d, axis=1) to find the minimum values along each row.
"""

import numpy as np

# Create a 2D NumPy array
arr_2d = np.array([[3, 8, 2], [5, 10, 7], [1, 6, 4]])

# Find the minimum value in the entire array
min_value = np.min(arr_2d)
print("Minimum Value in the Entire Array:")
print(min_value)

# Find the minimum value along each column (axis=0)
min_values_along_columns = np.min(arr_2d, axis=0)
print("\nMinimum Values Along Columns (axis=0):")
print(min_values_along_columns)

# Find the minimum value along each row (axis=1)
min_values_along_rows = np.min(arr_2d, axis=1)
print("\nMinimum Values Along Rows (axis=1):")
print(min_values_along_rows)