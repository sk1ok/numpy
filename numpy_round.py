"""
We create a NumPy array arr_float with floating-point numbers.
We use np.round(arr_float) to round the elements to the nearest integer.
We use np.round(arr_float, decimals=2) to round the elements to two decimals.
"""

import numpy as np

# Create a NumPy array with floating-point numbers
arr_float = np.array([2.345, 7.891, 4.123, 9.567])

# Round the elements to the nearest integer
rounded_integers = np.round(arr_float)
print("Rounded to Nearest Integer:")
print(rounded_integers)

# Round the elements to two decimals
rounded_decimals = np.round(arr_float, decimals=2)
print("\nRounded to Two Decimals:")
print(rounded_decimals)
