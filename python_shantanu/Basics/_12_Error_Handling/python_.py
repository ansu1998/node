# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# print(x)

# try:
#   print(x)
# except:
#   print("error fixed")



# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:



# x=10
# try:
#   print(x)
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")



# finally block

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


# try:
#   f = open("demofileing.txt","w")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")  



# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.
# The raise keyword is used to raise an exception.

# You can define what kind of error to raise, and the text to print to the user.

# x = 1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


# x = "hello"
# if  type(x) is str:
#   print("hii")
#   raise TypeError("Only integers are allowed")


# try:  
#   print("raising exception")
#   raise ZeroDivisionError
#   # raise AttributeError

# except ZeroDivisionError:
#   print("hi")

# # except AttributeError:
# #   print("attribute error is raised")

# except: 
#   print("hello")



