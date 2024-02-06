"""
We create a 2D NumPy array (arr_2d) with some values.
We use np.median(arr_2d) to calculate the median of the entire array.
We use np.median(arr_2d, axis=0) to calculate the median along each column.
We use np.median(arr_2d, axis=1) to calculate the median along each row.
"""

import numpy as np

# Create a 2D NumPy array
arr_2d = np.array([[3, 8, 2], [5, 10, 7], [1, 6, 4]])

# Calculate the median of the entire array
median_value = np.median(arr_2d)
print("Median of the Entire Array:")
print(median_value)

# Calculate the median along each column (axis=0)
median_values_along_columns = np.median(arr_2d, axis=0)
print("\nMedian Along Columns (axis=0):")
print(median_values_along_columns)

# Calculate the median along each row (axis=1)
median_values_along_rows = np.median(arr_2d, axis=1)
print("\nMedian Along Rows (axis=1):")
print(median_values_along_rows)
