"""
np.insert(arr, obj, values, axis=None)
array: Input array.
obj: Index before which values is inserted.
values: Values to insert into arr.
axis: Axis along which to insert values. If axis is None, arr is flattened first.
axis=0: Insert along rows (for 2D array, adds new rows).
axis=1: Insert along columns (for 2D array, adds new columns).
"""

import numpy as np

"""Inart 1D array"""
# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# print("Original array:", arr)
# new_arr = np.insert(arr, 2, 90)
# print("Array after insertion:", new_arr)

"""Inart 2D array"""

# arr_2d = np.array([[10, 20], [30,40]])
# print("Original array:\n", arr_2d)
# new_arr2d = np.insert(arr_2d, 1, [50,60], axis=0) # Insert along rows (axis=0)    
# print("Array after insertion along rows (axis=0):\n", new_arr2d)

# arr_2d = np.array([[10, 20], [30,40]])
# print("Original array:\n", arr_2d)
# new_arr2d = np.insert(arr_2d, 1, [50,60], axis=1) # Insert along columns (axis=1)
# print("Array after insertion along columns (axis=1):\n", new_arr2d)

# arr_2d = np.array([[10, 20], [30,40]])
# print("Original array:\n", arr_2d)
# new_arr2d = np.insert(arr_2d, 1, [50,60], axis=None) # Insert with axis=None (flattens the array first)
# print("Array after insertion with axis=None:\n", new_arr2d)


"""
Append values at the end of the array
"""
# arr = np.array([1, 2, 3, 4, 5])
# print("Original array:", arr)
# new_arr = np.append(arr, [6, 7, 8])
# print("Array after appending values:", new_arr)

"""Concat two arrays"""

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print("Original array:\n", arr)
# arr2 = np.array([[7, 8, 9], [10, 11, 12]])
# new_arr = np.concatenate((arr, arr2), axis=0)  # Concatenate along rows (axis=0)
# print("Array after concatenation along rows (axis=0):\n", new_arr)
# new_arr = np.concatenate((arr, arr2), axis=1)  # Concatenate along columns (axis=1)
# print("Array after concatenation along columns (axis=1):\n", new_arr)
# new_arr = np.concatenate((arr, arr2), axis=None)  # Concatenate with axis=None (flattens the arrays first)
# print("Array after concatenation with axis=None:\n", new_arr)

"""Remove elements from an array"""

# arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# print("Original array:", arr)
# new_arr = np.delete(arr, [2, 5])  # Remove elements at index 2 and 5
# print("Array after deletion:", new_arr)

"""Remove elements from a 2D array along a specified axis"""
# arr_2d = np.array([[10, 20], [30, 40], [50, 60]])
# print("Original 2D array:\n", arr_2d)
# new_arr2d = np.delete(arr_2d, 1, axis=0)  # Remove the second row (index 1)
# print("2D Array after deleting second row (axis=0):\n", new_arr2d)
# new_arr2d = np.delete(arr_2d, 0, axis=1)  # Remove the first column (index 0)
# print("2D Array after deleting first column (axis=1):\n", new_arr2d)
# new_arr2d = np.delete(arr_2d, 2, axis=None)  # Remove the third element in the flattened array
# print("2D Array after deleting third element (axis=None):\n", new_arr2d)


"""
Stacking arrays vertically and horizontally
vstack: Stack arrays in sequence vertically (row-wise).
hstack: Stack arrays in sequence horizontally (column-wise).
"""
# arr1 = np.array([[1, 2, 3]])
# arr2 = np.array([[4, 5, 6]])

# print(np.vstack((arr1, arr2)))  # Vertical stacking
# print(np.hstack((arr1, arr2)))  # Horizontal stacking


"""
# Splitting arrays into multiple sub-arrays
np.split(ary, indices_or_sections, axis=0)
hsplit: Split array into multiple sub-arrays horizontally (column-wise).
vsplit: Split array into multiple sub-arrays vertically (row-wise).
"""

arr = np.array([10, 20, 30, 40, 50, 60 ])
print(np.split(arr, 3))  # Split into 3 equal parts

arr_2d = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90]).reshape(3, 3)
print("Original 2D array:\n", arr_2d)
print(np.vsplit(arr_2d, 3))  # Vertical split into 3 equal parts
print(np.hsplit(arr_2d, 3))  # Horizontal split into 3 equal parts  

