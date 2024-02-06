import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Sum of all elements in the array
total_sum = np.sum(arr)

# Sum along each column (axis=0)
column_sum = np.sum(arr, axis=0)

# Sum along each row (axis=1)
row_sum = np.sum(arr, axis=1)

# Display the results
print("Original array:")
print(arr)

print("\nTotal sum of all elements:", total_sum)

print("\nSum along each column:")
print(column_sum)

print("\nSum along each row:")
print(row_sum)
