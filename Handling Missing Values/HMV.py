import numpy as np

"""
Handling Missing Values in Data
This module provides functions to handle missing values in datasets.
It includes methods for removing missing values, imputing missing values with mean, median, or mode,
and advanced imputation techniques using K-Nearest Neighbors (KNN).
np.isnan() is used to identify missing values in numerical arrays. #isnan stands for "is Not a Number"
np.nan is used to represent missing values in numerical arrays. #nan stands for "Not a Number"
np.isinf() is used to identify infinite values in numerical arrays. #isinf stands for "is Infinite"
"""

"""
ISNAN
"""
# arr = np.array([1, 2, np.nan, 4, 5])

# print(np.isnan(arr))  # Output: [False False  True False False]

# print(np.nan == np.nan)  # Output: False➡️⬇️
# # Answer: In NumPy, np.nan is not equal to itself. This is because NaN (Not a Number) is defined to be unequal to any value, including another NaN.


"""NAN to NUM"""
# np.nan_to_num() is a function in NumPy that replaces NaN (Not a Number) values with zero and infinite values with large finite numbers. DEFAULT is 0

# arr = np.array([1, 2, np.nan, 4, 5, np.nan])
# print(np.nan_to_num(arr))  # Output: [1. 2. 0. 4. 5. 0.]
# print(np.nan_to_num(arr, nan=-1))  # Output: [ 1.  2. -1.  4.  5. -1.]
# print(np.nan_to_num(arr, nan=99))  # Output: [ 1.  2. 99.  4.  5. 99.]

"""ISINF"""
# isinf() is a function in NumPy that checks for infinite values in an array. It returns a boolean array indicating whether each element is infinite (True) or not (False).

# arr = np.array([1, 2, np.inf, 4, -np.inf, 5])
# print(np.isinf(arr))  # Output: [False False  True False  True False]

# # Replace infinite values with a finite number
# cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000)
# print(cleaned_arr)  # Output: [   1.    2. 1000.    4. -1000.    5.]