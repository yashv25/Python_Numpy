import numpy as np

"""
# Indexing 
array[index] - Access a single element in 1d array
array[row, col] - Access a single element in 2d array
"""


arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# print(arr[0])  # Access first element
# print(arr[-1]) # Access last element


""" 
# Slicing
array[start:end] - Access elements from start index to end index-1
array[start:end:step] - Access elements from start index to end index-1 with a
"""

# print(arr[1:5])  # Access elements from index 2 to 6 step of 1
# print(arr[1:8:2])  # Access elements from index 2 to 8 step of 2 step of 2
# print(arr[:5])  # Access elements from start to index 5 
# print(arr[::2]) # Access all elements with step of 2
# print(arr[::-1]) # Access all elements in reverse order  


""" 
# Fancy Indexing
array[[index1, index2, ...]] - Access multiple elements using a list of indices
array[[row1, row2], [col1, col2]] - Access multiple elements in 2d array using lists of row and column indices
"""
# print(arr[[1, 3, 5]])  # Access elements at index 1, 3, and 5

"""
# Filtering data using boolean indexing/ masking    
condition = array > value - Create a boolean array based on a condition
array[condition] - Access elements that satisfy the condition
"""
print(arr[arr > 25])  # Access elements greater than 25
