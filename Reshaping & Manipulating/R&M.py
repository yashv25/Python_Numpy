import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

"""
# Reshape(rows, columns) specifies the new shape of the array if dimensions match \
reshaping does not return copy of the array but a view of the original array
"""

# reshaped_arr = arr.reshape(2, 3)
# print(reshaped_arr)

""" 
# flattening array: converting multi-dimensional array to 1D array
flatten() and ravel() functions are used for flattening
ravel() returns a view of the original array,
flatten() returns a copy of the original array
"""

# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr_2d.ravel())  # returns a view
# print(arr_2d.flatten())  # returns a copy   



