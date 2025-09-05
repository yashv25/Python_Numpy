import numpy as np

#creating arrays from python lists

#1#np.array([ele1,ele2,el3])

# arr = np.array([1,2,3,4,5])  
# print(arr)
# print(type(arr))

#2#with default values
#np.zeros(size) (3) fir 1d, (3,3) for 2d
# zeroes_array = np.zeros(3)
# print(zeroes_array)

# ones(shape)
# ones_array = np.ones((2,3))
# print(ones_array)

# full(shape,fill_value)
# filled_array = np.full((2,2),7)
# print(filled_array)

# creatigng arrays with sequences of numbers in numpy
# np.arange(start,stop,step)
# arr = np.arange(1,10,2)
# print(arr)

# creating identity matrix
# np.eye(n)
# identity_matrix = np.eye(4)
# print(identity_matrix)

# creating arrays with random values
# np.random.rand(d0,d1,d2,...,dn)  #uniform distribution    
# random_array = np.random.rand(3,2)
# print(random_array)