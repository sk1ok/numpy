"""
np.random.random() generates a random float between 0 and 1.
np.random.randint(1, 11) generates a random integer between 1 and 10.
np.random.randint(1, 101, size=5) generates an array of 5 random integers between 1 and 100.
np.random.rand(2, 3) generates a 2x3 array of random floats between 0 and 1.
np.random.shuffle(original_array) shuffles the elements of an array in-place.
"""

import numpy as np

# Generate a random float between 0 and 1
random_float = np.random.random()
print("Random Float between 0 and 1:")
print(random_float)

# Generate a random integer between 1 and 10
random_integer = np.random.randint(1, 11)
print("\nRandom Integer between 1 and 10:")
print(random_integer)

# Generate an array of 5 random integers between 1 and 100
random_integers_array = np.random.randint(1, 101, size=5)
print("\nArray of 5 Random Integers between 1 and 100:")
print(random_integers_array)

# Generate a 2x3 array of random floats between 0 and 1
random_floats_array = np.random.rand(2, 3)
print("\n2x3 Array of Random Floats between 0 and 1:")
print(random_floats_array)

# Shuffle the elements of an array
original_array = np.array([1, 2, 3, 4, 5])
np.random.shuffle(original_array)
print("\nShuffled Array:")
print(original_array)