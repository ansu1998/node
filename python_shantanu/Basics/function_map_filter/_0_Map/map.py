
# map(function, iterable)

'''
function: This is the function that you want to apply to each item in the iterable.
iterable: This is the iterable (e.g., a list, tuple, or string) that you want to apply the function to.
        The map() function returns an iterator (specifically, a map object in Python 3) 
        that can be converted to other iterable types like a list or tuple using functions like list() or tuple().


'''

# Square all elements in a list

# def  func1(x):
#     return x**2

# numbers = [1,2,3,4,5]
# square_numbers = map(func1,numbers)
# square_numbers_list = list(square_numbers)
# print(square_numbers_list)


# def  func1(x):
#     list1 =[]
#     for i in x:
#         k = i**2
#         list1.append(k)
#     print(list1)

# numbers = [1,2,3,4,5]
# func1(numbers)




#2,  Convert a list of strings to uppercase:
# def upper_case(x):
#     return x.upper()

# list1 = ["hello", "world", "python"]
# map1 = map(upper_case,list1)
# list1 = list(map1)
# print(list1)



# def upper_case(list1):
#     s=[]
#     for i in list1:
#         a= i.upper()
#         s.append(a)
#     print(s)

# list1 = ["hello", "world", "python"]
# upper_case(list1)






