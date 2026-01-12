# A function is a block of code which only runs when it is called

'''
syntax 

def function_name():
    statment

function_name()

'''
# def funct1(a,b,c,d):
#     # a=10
#     # b=20
#     print(a+b+c)
    
# funct1(10,20,40,60)

# a=10
# b=20
# if a<b:
#     pass
    


# def add1(a,b,c,d):
#     print(a+b+c)
#     print(d)
# add1(10,20,30,50)



# def display(a,b,c,d,e):
#     print(a+b+c)
    
# display(20,30,40,10,8)



# def add(a,b,c):
#     print("sum of n1 and n2 is",a+b+c)
   
# add(10,20,30)
# add(10,20,60)

# # 
# def ansu(n1):
#     print("my name is : " ,n1)
# ansu("ansu")
# def funct1(a,b,c,d):
#     # a=10
#     # b=20
#     print(a+b+c)
    
# funct1(10,20,40,60)

# def display_name(name,name1):
#     n1= input("enter a name:")
#     print('your name is ',name,name1,n1)

# display_name('jerry','sam')

# def funct2(*list1):
#     sum1=0
#     for i in list1:
#         sum1 = sum1+i
#     print(sum1)
# funct2(9,8,9,10)

# function with arbitrary argument

def add(*num):
    for i in num:
        print(i)
add(2,1,8,5,10,6,7,10,5)


# keyword argument

def emp(name,salary):
    print('Name:',name)
    print('Salary:', salary)

emp(salary="1000",name="ansu")

# sum of numbers (1,2,3,4,10,8,11,20)
# largest (5,2,3,7,8,9,4) using arbitary arguments

# def larg(*num):
#     first = num[0]
#     for i in num:
#         if i>first:
#             first=i
#     print(first)
# larg(5,2,3,7,8,9,4)

# default argument
 
# def add(a,b,c=1):
#     print(a+b+c)
# add(1,3,2)


# def person_details(name='anonymous',age=0):
#     print('Name: ',name)
#     print('age: ', age)

# person_details()


# arbitrary keyword arugment

# def store(**product):
#     print(product)
#     print(product['Price'])

# store(item='Apple',Price=110,color='Green',qty='1kg')


# dictn = {'item': 'Apple', 'Price': 110, 'color': 'Green', 'qty': '1kg'}
# print(dictn["item"])

# def my_function(**kid):
#     print("His last name is " + kid["lname"])
#     print(kid)

# my_function(fname = "Tobias", lname = "yyy")

# Return = Sends a value back to the caller of the function.
# print  = Does not send any value back to the caller.


# def add(a, b):
#     return a + b

# # Calling the function
# result = add(3, 4)
# print("Result using return:", result)


# def add(a, b):
#     print("The sum is:", a + b)

# # Calling the function
# result = add(3, 4)
# print("Result using print:", result)

# def c(x, y):
#     if x % y :
#          return x+5
#     else:
#         return y+10
# print(c(20, 5))



# def sum(*num):
#     sum=0
#     for i in num:
#         sum = sum + i
#     return sum

# print(sum(1,2,3,4,10,8,11,20))


# def largest(*num):
#     l = num[0]
#     for i in num:
#         if l>i:
#             l=i
#     print('largest of :',l)

# largest(5,2,3,7,8,9,4)


# call by value
# If the argument is immutable (like numbers, strings, tuples), 
# it's passed by value. Changes inside the function 
# don't affect the original value.

# def modify_value(x):
#     x = x + 10
#     print("Inside function:", x) 

# a = 10
# modify_value(a)
# print("Outside function:", a)     
  

# def change(x):
#     x = 'This is a new value'
#     print(x)

# a='my name is kelvin'
# change(a)
# print(a)


# def change(x):
#     x = 60.5

# a=30.5
# change(a)
# print(a)



# # call by reference
# If the argument is mutable (like lists, dictionaries),
# it's passed by reference. Changes inside 
# the function affect the original value.

# def change_list(lst):
#     lst.append(4)
#     print(lst)

# my_list = [1, 2, 3]
# change_list(my_list)
# print(my_list)  

# def modify_dict(d):
#     d['age'] = 25
#     d['city'] = 'New York'
#     print("Inside function:", d)

# # Original dictionary
# my_dict = {'name': 'Ansu'}
# modify_dict(my_dict)
# print("Outside function:", my_dict)



# def myFun(**kwargs):
    # for key, value in kwargs.items():
#         print("{0} == {1}".format(key, value))
 
# myFun(first='Geeks', mid='for', last='Geeks')


# def fun(n1,n2):
#     for x in range(n1,n2+1):
#         if x%4==0:
#             print(x, end=" ")
# fun(100,120)


# return in function 

# def funct1():
#     print("hello")
#     print("hi")

# funct1()

# return terminate a function
# def funct2():
#     return("hello")
#     return("hi")

# print(funct2())


# Another concept - assign a value to variable
# def twice(x):
#     print(2*x)
# # twice(4)
# s= twice(4)
# # print(s)

# def double(n):
#     return 2*n
# # print(double(5))
# d= double(5)
# print(d)





# question
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string. 

# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


