import numpy as np

random_array = np.random.randn(25)

min_value = random_array.min()
max_value = random_array.max()
min_index = random_array.argmin()
max_index = random_array.argmax()

print("Array:", random_array)
print("Min value:", min_value, "at index", min_index)
print("Max value:", max_value, "at index", max_index)
