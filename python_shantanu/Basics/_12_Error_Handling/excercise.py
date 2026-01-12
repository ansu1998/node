# x = 5
# y = "hello"
# # print(x+y)
# try:
#     z = x + y 
# except TypeError as v:
#     print("it is wrong1")
# except Exception as t:
#     print("it is wrong")



# def fun(a):
#     if a < 4:
#         a = a/(a-3) 	
#         print("Value of b = ", a)	
# fun(3) 

 

# def fun(a):
#     try:
#         if a < 4: 
#             b = a/(a-3) 	
#         print("Value of b = ", b)
#     except ZeroDivisionError as v:
#         print("it is wrong1")
#     except Exception as v:
#         print("it is wrong",v)
	
# fun(3) 
# fun(5) 

# def calculate_value(x, y):
#     try:
#         result = x / (x - y)  
#         print(f"Result: {result}")
#     except ZeroDivisionError:
#         print("Error: Division by zero occurred. (x - y) cannot be zero.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Function calls
# calculate_value(5, 5)  
# calculate_value(10, 2)  
# calculate_value("a", 2) 

# def AbyB(a , b): 
#     c = ((a+b) / (a-b))
#     print (c) 

# AbyB(2.0, 3.0) 
# AbyB(3.0, 3.0) 




# def AbyB(a , b): 
# 	try: 
# 		c = ((a+b) / (a-b)) 
# 	except ZeroDivisionError: 
# 		print ("a/b result in 0") 
# 	else: 
# 		print (c) 


# AbyB(2.0, 3.0) 
# AbyB(3.0, 3.0) 






# def fun(a): 
# 	if a < 4: 
# 		b = a/(a-3) 

# 	print("Value of b = ", b) 
	
# try: 
# 	# fun(3) 
# 	fun(5) 


# except ZeroDivisionError: 
# 	print("ZeroDivisionError Occurred and Handled") 
# except UnboundLocalError: 
# 	print("NameError Occurred and Handled")



