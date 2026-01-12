'''

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
It describes the idea of wrapping data and the methods that work on data within one unit. 

# access modifiers(method in encapsulation)

public-  b

protected - _b

private - __b

'''


# public
# all access

# class A:

#     def __init__(self):
#         self.a = 1
#         self.b = 2 
#         self.c = 3

# a=A()
# print(a.a,a.b,a.c)

# protected
# access all packages in class


# class A:

#     def __init__(self):
#         self.a = 1
#         self._b = 2 
#         self.c = 3

#     def myfun(self):
#         print(self._b)

# a = A()
# print(a.a, a._b)
# a.myfun()


# private
# Private members are similar to protected members, the difference is that the class members declared private 
# should neither be accessed outside the class nor by any base class. 
# In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.

# class A:

#     def __init__(self):
#         self.a = 1
#         self._b = 2 
#         self.__c = 3

#     # def _display(self):
#     #     print(self.__c)

#     def __display(self):
#         print(self.a)

# a = A()
# # print(a.a, a._b,a.__c)
# # print(a.a, a._b)
# # a._display()

# a.__display()




# dic={}
# sr1=input('enter your string:')
# for i in sr1:
#     a=sr1.count(i)
#     dic.update({i:a})
# print(dic)


# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))




# 11,Write a Python program to get a single string from two given strings,
#  separated by a space and swap the first two characters of each string. 
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

# def chars_mix_up(a, b):
#   new_a = b[:2] + a[2:]
#   new_b = a[:2] + b[2:]

#   return new_a + ' ' + new_b
# print(chars_mix_up('abc', 'xyz'))



# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

# def change_sring(str1):
#       return str1[-1:] + str1[1:-1] + str1[:1]
	  
# print(change_sring('abcd'))
# print(change_sring('12345'))


# Write a Python function to get a string made of 4 copies of the last two characters of a specified string 
# (length must be at least 2).



# def insert_end(str):
# 	sub_str = str[-2:]
# 	return sub_str * 4

# print(insert_end('Python'))
# print(insert_end('Exercises'))



# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
# which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

def romanToInt(s):
    d={'':0,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result=0
    prev=0

    for c in s[::-1]:
        current = d[c]
        if current<prev:
            result-=current
        else:
            result+=current
        prev = current

    return (result)
a=romanToInt("LVIII")
a1=romanToInt("MCMXCIV")

print(a)
print(a1)


#  Write a Python program to select the odd items of a list

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(x[::2])



# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# def twoSum(nums, list1,target):
#     for i in list1:
#         if num[i] =