# Logical Error
# syntax Error

# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# x=10
try:
    print(x)
except:
    print("it is handled")


# # x=10
# try:
#     print(x)
# except:
#     print("this is handled")

# a=5
# b=2
# try:
#     print(a/b)
# except:
#     print("infinity")
# else:
#     print("hi")
# finally:
#     print("final")


# a=5 
# # b=2
# # b=0
# try:
#     print(a/b)
# except Exception as E: 
#         print("Bye",E)
# finally:
#     print("not depent")


# try:
#     print(x)
# except Exception as r:
#     print("Hey , You cannot divide a Number by Zero : ", r)

# print("BYE")


# a=5
# # b=2
# b=0
# try:
#     print(a/b)
# except Exception as e:
#     print("Hey , You cannot divide a Number by Zero :",e)
# finally:
#     print("BYE")


# a=5
# # b=0
# b=2 
# # k= int(input("Enter a number "))
# try:
#     print("Resource Open")
#     k= int(input("Enter a number "))
#     print(k)
#     print(a/b)
#     print("Resource Closed")
# except Exception as e:
#     print("Hey , You cannot divide a Number by Zero :",e)
# finally:
#     print("finally Resource Closed")


# print(x)
# x=2
# b=0
# try:
#     print(x/b)
# except ZeroDivisionError as e:
#     print("Hey , You cannot divide a Number by Zero :",e)
# except NameError as e:
#     print("Name Error is :",e)
# except Exception as e:
#     print("Any Exception",e)


# try:
#     print(x)
# except Exception:
#     print("Exception")



# # Finally block will be executed  if we get Error as well as if we don't get the Eroor
a=5
# b=0
b=6
# k= int(input("Enter a number : "))
# print(k)
try:
    print("Resource Open")
    print(a/b)
    k= int(input("Enter a number: "))
    print(k)    
except ZeroDivisionError as e:
    print("Hey , You cannot divide a Number by Zero :",e)
except ValueError as v:
    print("Invalid input")
except Exception as v:
    print("Something went Wrong",v)
finally:
    print("Resource Closed")
    

