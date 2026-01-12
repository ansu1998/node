# os module
# This module has functions to perform many tasks of operating system.


# Return a string repreting the currently working directory.
import os
print(os.name)


# get current working directory
print(os.getcwd())

# The os module has listdir() function which returns list of all files in specified directory.
print(os.listdir())
# 

# We can create a new directory using mkdir() function from os module.
# import os
# os.mkdir('Sam1')
# print(os.listdir())

# os.mkdir('a/b')  

# 
# os.makedirs('a/b')

# print(os.listdir())

# rename the files
os.rename('a','c')
# print(os.listdir())

# os.makedirs('f')


# The rmdir() function in os module removes a specified directory either with absolute or relative path. 
# However it should not be the current working directory and it should be empty.
# os.rmdir('f')
# os.rmdir('c/b')

os.removedirs('x/z')

# os.removedirs('ansu/o')
print(os.listdir())










