"""
We create a NumPy array arr_float with floating-point numbers.
We use np.floor(arr_float) to round down each element to the nearest integer.
"""

import numpy as np

# Create a NumPy array with floating-point numbers
arr_float = np.array([2.345, 7.891, 4.123, 9.567])

# Apply the floor function to round down to the nearest integer
floored_values = np.floor(arr_float)
print("Floored Values:")
print(floored_values)
