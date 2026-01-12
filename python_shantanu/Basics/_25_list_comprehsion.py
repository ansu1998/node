# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based 
# on the values of an existing list.

# newlist = [expression for item in iterable if condition == True]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = []
for i in fruits:
    new.append(i)
print(new) 


# new_1 = [i for i in fruits]
# print(new_1)

newlist = [x for x in range(10)]
print(newlist)


a = [1,3,5,7,9,11]
# list3=[]
# for i in a:
#     list3.append(i*2)
# print(list3)

new = [i*2 for i in a]
print(new)


ele = [i**2 for i in range(1,7)]
print(ele)

lst_1 = ['one','two','three','four','one','one']
newlist = []
for x in lst_1:
  if x != 'one':
    newlist.append(x)
print(newlist)


# newlist = [expression for item in iterable if condition == True]

lst_1 = ['one','two','three','four','one','one']
lst_1 = [item for item in lst_1 if item != 'one']
print(lst_1)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

# fruits = ['apple', 'banana', 'cherry']
# indexed_fruits = [(index, fruit) for index, fruit in enumerate(fruits)]
# print(indexed_fruits)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# list2 = []
# for i in fruits:
#     if "n" not in i:
#         list2.append(i)
# print(list2)

s = [i for i in fruits if "n" not in i]
print(s)

# s = [statment1 if <condition> else statment2 for <variable> in <iterable>]

s = [i if "n" not in i else "hi" for i in fruits ]
print(s)


# fruits = ['apple', 'banana', 'cherry', 'mango']
# characters = 'xyz'

# s = [f"{fruit}-{char}" if "n" not in fruit else f"{fruit}-Excluded" for fruit in fruits for char in characters]
# print(s)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # newlist = []
# # for x in fruits:
# #   if "a" in x:
# #     newlist.append(x)
# #   else:
# #     print("hi")
# # print(newlist)


# new = [x  if "a" in x else "hi" for x in fruits]
# print(new)