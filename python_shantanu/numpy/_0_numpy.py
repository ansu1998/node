# Numpy

# NumPy is a Python library used for working with arrays.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions 
# that make working with ndarray very easy.
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.


# Installation of NumPy
# pip install numpy


# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)


# Create a 1-D array containing the values 1,2,3,4,5:

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)


# 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.
# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)


# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6

# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)


# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that 
# returns an integer that tells us how many dimensions the array have.

# import numpy as np
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)


# Higher Dimensional Arrays
# An array can have any number of dimensions.

# When the array is created, you can define the number
# of dimensions by using the ndmin argument.

# Create an array with 5 dimensions and verify that it has 5 dimensions:

# import numpy as np
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('number of dimensions :', arr.ndim)