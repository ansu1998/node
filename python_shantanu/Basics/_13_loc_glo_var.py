
# The location where we can find a variable and also access it if required is called the scope of a variable.
# Variables that are created outside of a function are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.
# Local variables in python are those variables that are declared inside the function. 



# local variable b
# def fun():
#     b=10
#     print(b)
# fun()
# print(b)


# global variable c
# def fun():
#     b=10
#     print(c)
#     print(b)
# c=20
# fun()
# print(c)



# global 

# def fun():
#     global a1
#     a1=20
#     print(a1) 
# a1=10
# fun()
# print(a1)


# x = "awesome"
# def myfunc():
#   print("Python is " + x)

# x="fantastic"
# myfunc()
# print(x)


# x = "awesome"
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()
# print("Python is .." + x)



# x = "awesome"
# def myfunc():
# #   global x
#   x = "fantastic"
#   print("Python is " + x)

# x='hiii'
# myfunc()
# print("Python is " + x)




# def function1():
#     q = 900 
#     print(q)
# function1()
# print(q)


# a = 1 # global variable
# def f2():
#     print(a)

# f2()
# print(a)


# b = 10
# def f3():
#     b = 11
#     print(b)
# b=30
# f3()
# print(b)
# priority more for local  variable



# x = 'global'
# def outer():
#     # x = 'enclosed'
    
#     def inner():
#         # x = 'local'
#         print(x)
#     inner()
    
# outer()




# Priority : Local, Enclosed, Global, Built in (LEGB)




