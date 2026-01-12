# map 
# The map() function is used to apply a function to all elements in an iterable
#  (like a list, tuple, or set) without using explicit loops.

def  square_root(n):
    # return n**(1/2)
    return n*2
print(square_root(9))


nums = [16,25,49,100,121]
# Square root of each number


# syntax
# map(function_base, iterable)

map_object =  map(square_root, nums)
print(list(map_object))

# list1 =[]
# for i in nums:
#     list1.append(int(i**(1/2)))
# print(list1)
# # Eg:

# print(list(map(lambda x:x**(1/2), nums)))


# filter
# The filter() function is used to filter elements from an iterable 
# based on a condition.

# def odd1(n):
#     return n%2==1
# print(odd1(3))
# print(odd1(2))


# nums = [16,25,49,100,121]
# print(list(filter(odd1, nums)))


# reduce

# list1=[10,11,12,13]

# def add(a,b):
#     return a+b

# from functools import reduce

# print(reduce(add, list1))


