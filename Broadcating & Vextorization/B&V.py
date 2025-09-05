import numpy as np

# prices = np.random.randint(100, 1000, size=30) # Random prices between 100 and 1000
# discount = 10 # 10% discount
# print("Original Prices:", prices)
# final_prices = prices * (1 - discount / 100)
# print("\nFinal Prices:",final_prices)

"""Broadcasting"""

# arr = np.array([100, 200, 300])
# result = arr * 2 # Broadcasting the scalar 2 across the array
# print(result)  # Output: [200 400 600]

""""1d to 2d array"""
# matrix = np.array([[1, 2, 3], [4, 5, 6]]) # 2D array
# vector = np.array([10, 20, 30]) # 1D array

# result = matrix + vector # Broadcasting the 1D array across the 2D array
# print(result)  # Output: [[11 22 33] [14 25 36]]

"""Error in broadcasting"""
# arr1 = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
# arr2 = np.array([10, 20]) # Shape (2,)
# result = arr1 + arr2 # This will raise an error due to incompatible shapes
# # by reshaping the second array to (2, 1) we can make it compatible for broadcasting



""" Vectorization """
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6 ])
# result = arr1 + arr2 # Element-wise addition
# print(result)  # Output: [5 7 9]

# arr1 = np.array([10, 20, 30 ])
# multiply = arr1 * 3 # Element-wise multiplication   
# print(multiply)  # Output: [30 60 90]   