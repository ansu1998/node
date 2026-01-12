'''
Tuple 
----------

Tuples are used to store multiple items in a single variable.
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Tuples are written with round brackets.
'''

# tup1 = ('red','green','red',6,'blue')
# print(type(tup1))


# print(tup1[0])

# print(tup1[1:])
 

# not support
# tup1[0]='black'
# print(tup1)


# tup1 = ('red','green','red',6,'blue',[1,3,4])
# print(tup1.index('red'))
# print(tup1.index('red', 1))


# print(tup1.count('red'))

# not support
# del tup1[0]
# print(tup1)

# del tup1
# print(tup1)

# not support
# tup1 = ('red','green','red',6,'blue',[1,3,4])
# tup1.append('pink')
# print(tup1)


# tup1 = ('red','green','blue','red')
# for i in tup1:
#     print(i)

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

# tup1 = ('red','green','red','blue')
# i=0
# while i < len(tup1):
#     print(tup1[i])
#     i = i+1
    

# Write a Python program to find the repeated items of a tuple.
# tuple = (1, 1, 2, 3, 4, 4, 5)

myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
print(x)


# Write a Python program to add an item to a tuple.
myTuple = ("John", "Peter", "Vicky")
v = list(myTuple)
v.append("sam")
new = tuple(v)
print(new)


# Write a Python program to remove an item from a tuple.




# tup1 = ('red','green','red',6,'blue',[1,3,4])
# v=list(tup1)
# v[0] = "black"
# v.append("black")
# t=tuple(v)
# print(t)

# tup1 = ('red', 'green', 'red', 6, 'blue', [1, 3, 4])
# tup2 = tup1 + ('black',)
# print(tup2)


# tup1 = ('red', 'green', 'red', 6, 'blue', [1, 3, 4])
# tup2 = ('black',) + tup1[1:]
# print(tup2)

a=10
if a<0:
    pass

# Write a Python program to convert a tuple to a string.
# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# str = '#'.join(tup)
# print(str)


# Write a Python program to remove an item from a tuple.
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)


# a= "ansu"
# b = 12
# c= a*b
# print(c)


# l = int(input("enter no of element:"))
# lst = []
# for i in range(l):
#     lst.append(input())
# print(lst)


# Program to read a string and remove the given words from the string.
# enter your sentence: ansu is good
# removing word: good
#  ansu is


# Program to find the sum of all even numbers in a group of n numbers entered by the user.
# Enter total number:4
# 2
# 4
# 1
# 5
# sum is:  6

