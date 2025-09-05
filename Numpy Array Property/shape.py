import  numpy as np

# arr_1d = np.array([1, 2, 3, 4, 5])
# print(arr_1d.shape)  # Output: (5,)
# arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr_2d.shape)  # Output: (2, 3)  
# arr_3d = np.array([[[1,2], [3,4], [5,6], [7,8]]])
# print(arr_3d.shape)  # Output: (1, 4, 2)


# print(arr_1d.ndim)  # Output: 1
# print(arr_2d.ndim)  # Output: 2
# print(arr_3d.ndim)  # Output: 3


arr = np.array([ 1.2, 3.4, 5.6])
print(arr.dtype)  # Output: float64 
int_arr = arr.astype(int)
print(int_arr)  # Output: [1 3 5]
print(int_arr.dtype)  # Output: int64 
