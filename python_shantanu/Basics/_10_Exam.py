# Write a Python program to add 'ing' at the end of a given string (length should be 
# at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string 
# length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly


# def add_string(str1):
#   length = len(str1)

#   if length > 2:
#     if str1[-3:] == 'ing':
#       str1 += 'ly'
#     else:
#       str1 += 'ing'
#   print(str1)

# add_string('ab')
# add_string('abc')
# add_string('string')


# Write a Python program to get a single string from two given strings, separated by 
# a space and swap the first two characters of each string. 
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz


# def chars_mix_up(a, b):
#   new_a = b[:2] + a[2:]
#   new_b = a[:2] + b[2:]

#   print(new_a + ' ' + new_b)
# chars_mix_up('abc', 'xyz')


# Write a Python program to get a string from a given string where all occurrences of 
# its first char have been changed to '$', except the first char itself. 
# Sample String : 'restart'
# Expected Result : 'resta$t

# def change_char(str1):
#   char = str1[0]
#   str1 = str1.replace(char, '$')
#   str1 = char + str1[1:]

#   print(str1)

# change_char('restart')


# Write a Python program to count the number of characters (character frequency) 
# in a string. 
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#         print(dict)
# char_frequency('google.com')



# 1/04/2024
# Program to read list of names and sort the list in alphabetical order.

# n=int(input("Enter the number of names...."))
# names=[]
# print("Enter {} names".format(n))
# for i in range(n):
#    nam=input()
#    names.append(nam)
# names.sort()
# print(names)


'''
input will gives like 7564168

example separate odd place integers: 5,4,6

you have to return a 4 digit OTP by squareing the digits.


digits from above example: 5,4,6

square of those numbers: 25,16,36

so the otp to be returned is first four digits: 2516

# '''
# 7564168
num = input("Enter a numbers: ")
len_num = len(num)
otp =""
for i in range(1,len_num,2):
    odd = int(num[i])
    print(odd)
    odd1 = odd**2
    otp+=str(odd1)
print(otp[0:4])


x = [7, 5, 6, 4, 1, 6, 8]
y = []
for i in range(1, len(x), 2):
    y.append(str(x[i] ** 2))
    if len(y) == 4:
        break

# Combine the first four squared digits to form the OTP
otp = int(''.join(y))
print("OTP:", otp)


'''
Write a Python program to count the number of strings where the string length is 2 or more and 
the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

# list_0 = ['abc', 'xyz', 'aba', '1221','cbc']
# count=0
# for i in list_0:
#     if len(i)>=2 and i[0]==i[-1]:
#         count=count+1
# print(count)


# Write a Python program to get a single string from two given strings, separated by a space and 
# swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


# def chars_mix_up(a, b):
#   new_a = b[:2] + a[2:]
#   new_b = a[:2] + b[2:]

#   return new_a + ' ' + new_b
# print(chars_mix_up('abc', 'xyz'))
