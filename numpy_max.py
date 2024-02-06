"""
We create a 2D NumPy array (arr_2d) with some values.
We use np.max(arr_2d) to find the maximum value in the entire array.
We use np.max(arr_2d, axis=0) to find the maximum values along each column.
We use np.max(arr_2d, axis=1) to find the maximum values along each row.
"""

import numpy as np

# Create a 2D NumPy array
arr_2d = np.array([[3, 8, 2], [5, 10, 7], [1, 6, 4]])

# Find the maximum value in the entire array
max_value = np.max(arr_2d)
print("Maximum Value in the Entire Array:")
print(max_value)

# Find the maximum value along each column (axis=0)
max_values_along_columns = np.max(arr_2d, axis=0)
print("\nMaximum Values Along Columns (axis=0):")
print(max_values_along_columns)

# Find the maximum value along each row (axis=1)
max_values_along_rows = np.max(arr_2d, axis=1)
print("\nMaximum Values Along Rows (axis=1):")
print(max_values_along_rows)
