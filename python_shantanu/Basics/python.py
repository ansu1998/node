# list1 = [1,2,"apple",3,3.6]
# print(list1)

# list1.append(9)
# print(list1)

# tuple1 = (1,2,4,5)

# dict1 = {"apple":2,"orange":5,"3":9,"cat":"9"}
# print(dict1)

# dict1["green"]=2
# print(dict1)



# class Employee(models.Model):

#     Person=models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

# obj1 = Employee()
# obj1.Person






# import mymodule
# mymodule.greeting("Jonathan")


# a = mymodule.person1["age"]
# print(a)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1::2])

from mymodule import *

funct(person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
  })

'''
Built-in Modules
----------------------------------------
'''


'''
The Platform module is used to retrieve as much possible information about the platform on which the 
program is being currently executed.

'''
# import platform
# x = platform.system()
# print(x)



# Using the dir() Function

# The dir() function returns all properties and methods of the specified object, without the values.

# This function will return all the properties and methods,
#  even built-in properties which are default for all object.


# There is a built-in function to list all the function names (or variable names) in a module. 
# The dir() function:

# import platform
# x = dir(platform)
# print(x)



#str1=('sample string:restart')
#str0=('expected result:resta$t')
#for i in str0:
#    i(0)=='$'

#print(str0)


# lst1=('abc')
# for i in lst1:
#     i='ing'
#     print('abc'+i)

# lst2=('string')
# for i in lst2:
#   if i='ing'
#     print(i)