"""
We create a 2D NumPy array (arr_2d) with some values.
We use np.mean(arr_2d) to calculate the mean of the entire array.
We use np.mean(arr_2d, axis=0) to calculate the mean along each column.
We use np.mean(arr_2d, axis=1) to calculate the mean along each row.
"""

import numpy as np

# Create a 2D NumPy array
arr_2d = np.array([[3, 8, 2], [5, 10, 7], [1, 6, 4]])

# Calculate the mean of the entire array
mean_value = np.mean(arr_2d)
print("Mean of the Entire Array:")
print(mean_value)

# Calculate the mean along each column (axis=0)
mean_values_along_columns = np.mean(arr_2d, axis=0)
print("\nMean Along Columns (axis=0):")
print(mean_values_along_columns)

# Calculate the mean along each row (axis=1)
mean_values_along_rows = np.mean(arr_2d, axis=1)
print("\nMean Along Rows (axis=1):")
print(mean_values_along_rows)
