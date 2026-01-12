# 
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# name ='ansu'
# print(type(name))

str1 = "deepak"
new=""
for i in range(len(str1)-1,-1,-1):
    # print(str1[i], end="")
    new+=str(str1[i])
print(new)

# print(str1[::-1])
    

# name1 = '''
# my 
# dfgh
# cvbjn

# '''
# print(name1)
# a= '''
# cgfvhbjnkn
# ghbjk
# ghjbk
# gfhvjbnkml
# '''



# txt = 'welcome to python'
# print(len(txt))

# # indexing
# print(txt[0])
# print(txt[1])
# print(txt[6])


# slicing
# txt = 'welcome to python'
# print(txt[0:7])
# print(txt[-2])
# print(txt[0:])
# print(txt[:17])
# print(txt[:])
# print(txt[0:16:3])
# print(txt[::-1])
# print(txt[-8:-6])
# print(txt[-17:17])
# print(txt[])

# 0,3,6,9,12,15
# negative indexing
# print(txt[-1])
# print(txt[-2])

# # # # # Slice 
# txt = 'welcome to python'
# print(txt[0:7:2])

# print(txt[:7])

# print(txt[0:])

# print(txt[:])
# print(txt[8:10])

# print(txt[-5:-1])
# print(txt[::-1])



# txt = 'welcome to python'
# i=len(txt)-1
# while i>=0:
#     print(txt[i])
#     i=i-1

# for i in range(0,len(txt)):
#     print(txt[i])

# for i in range(len(txt)-1,-1,-1):   
#     print(txt[i])

# write prgm to reverse a string

# i= len(txt)-1
# while i>=0:
#     print(txt[i])
#     i= i-1


# for i in txt:
#     print(i)

# txt = 'ansuapillai'
# for i in range(0, len(txt)):
#     print(txt[i])

# for i in range(len(txt)-1,-1, -1):
#     print(txt[i], end="")


# for i in txt:
#     print(i)


# txt1 = "welcome"
# for i in range(0, len(txt1)):
#     print(txt1[i])


# for variable in iterable
# for i in txt1:
#     print(i)


# for i in range(len(txt1)-1,-1,-1):
#     print(txt1[i])



# txt = "welcome"
# print("hello greek"*3)


# for i in range(3):
#     print("hello greek")

# txt1="my name is sanju"
# for i in txt1:
#     print(i)

# for i in range(0,len(txt)):
#     print(txt[i])



# reverse using for loop

# capitalize

# s = 'welcome to python'
# print(s.capitalize())

# print(s.title())

# # # # # count
# print(s.count('o'))
# a=int(input("enter a number: "))
# fact=1
# for i in range(a,1,-1):
#     fact*=i
# print(fact)

# # # # find(str, start)
# s= 'Welcome, To python'

# print(s.find('To'))
# print(s.find('o',11))
# print(s.find('o',5, 11))

# # # # lowercase and uppercase
# print(s.lower())

# print(s.upper())
# print(s.swapcase())


# # # # # split
s= 'Welcome, To python'
print(s.split('e'))


# # # # #islower() 
# u='Python'
# print(u.islower())


# txt = "     banana     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")

# a = "Hello, World!"
# print(a.replace("W", "M"))

# myTuple = ("John", "Peter", "Vicky", "ansu")
# x = "*".join(myTuple)
# print(x)


# txt = "Hello, welcome to my world."
# x = txt.index("welcome")
# print(x)

string2 = 'Sam good'
j= string2.find(' ')
new= string2[0]+'.'+string2[j+1]
print(new.upper())


'''
Ansu jose
A.J


Ansu Pillai G
A.P.G

# '''

# string1 = "ansuuuuss"
# s=list(string1)
# for i in string1:
#     if s.count(i)

# h,e=1,None
# for i in s:
#     if s.count(i)>h:
#         h=s.count(i)
#         e=i
# print(e)


# name = input("Enter a name: ")
# pos = name.find(' ')
# short_name = name[0] +'.'+name[pos+1]
# print(short_name.upper())


# input_name = "Ansu Pillai G"
# parts = input_name.split()
# initials = [i[0] for i in parts]
# output_initials = ".".join(initials)
# print(output_initials)


# name = "Ansu Pillai G"
# initials = ""
# for word in name.split():
#     initials += word[0] + "."
#     print(initials)
# output_initials = initials[:-1] 
# print(output_initials)



# string and operator

# s0 = 'Hello'
# s1 = 'world'
# print(s0+' '+s1)
# print('21'+s1)
# print(str(21)+s1)
# print(s0+' '+s1+' hii')

# # print(s0-s1)

# print(s0*10)
# print(s0*s1)

# string formating (old style)

# a= 5
# b = 6
# print('sum of', a , 'and', b, 'is',a+b)
# print('substraction of', a, 'and',b, 'is',a-b)


# g = a+b
# print('sum is',h) 

# #  string formating(newstyle)
#

# a=10
# b=20
# print("sum  of",a,b,"is", a+b)

# name='adarsh'
# age = 24
# address = 'erkm'
# phone= '12345'
# # print('your name is', name, 'your age is', age)

# str2= 'sum is {}'.format(a+b)
# str1 = 'your name is {} and your age is {} and your address is {} and your phone number is {}'.format(name,age,address,phone)
# print(str1, str2)


# # #
# s = 'welcome,  {1}, your age is {0} and you address {2}'.format(name,age,address)
# print(s)


# str = 'hey {1}, your nick name is {0}'.format('anu','devi')
# print(str)


# # f-string
# name = 'anu'
# age = 23
# addr = 'erkm'
# phone=123344
# print(f"Hello, {name}, your age is {age} and address {addr} and your phone is {phone}")




'''
***
*****
**
******


anu jose 
A.J
'''
# list1 = [3,5,2,6]
# for i in list1:
#     print(i*'*')


# name ='Anu jose'
# pos = name.find(' ')
# new = name[0]+'.'+name[pos+1]
# print(new.upper())



# list2 = [3,5,2,6]
# for i in list2:
#     print(i*'*')
    

# pass
# a=1
# if a>10:
#     pass

'''
Python program to print even length words in a string 
srt1 = "this is a python"
'''



# srt1 = "this is a python"
# count=0
# new = srt1.split(' ')
# for i in new:
#     if len(i)%2==0:
#         count += 1
# print(count)
# print(i)

'''
****
*****
*******
**
***

'''
# list1 = [4,5,7,2,3]
# for i in list1:
#     print('*'*i)

# Pratical questions:

#1,  Write a Python program to get a string from a given string where all occurrences of its first char 
# have been changed to '$' except the first char itself.
'''
input = 'restartr'
output = resta$t$

'''
# str1 = "restartrr"
# char = str1[0]
# str1 = str1.replace(char, '$')
# str2 = char + str1[1:]
# print(str2)

# print(change_char('restart')) 

# 2,program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.
# input='abc', 'xyz'
# output=xyc abz


# a = 'abc'
# b = 'xyz'
# new_a = b[:2] + a[2:]
# new_b = a[:2] + b[2:]
# result = new_a + ' ' + new_b
# print(result)  


'''
****
*****
*******
**
***
'''

# list_1 = [5,6,7,2,3,8]
# for i in list_1:
#     print(i*"*")


# for i in str1:
#     print(i)

# for i in range(0,len(str1)):
#     print(str1[i])




# str1 = "ansu a pillai"
# for i in str1:
#     if i == 'a':
#         s=i.replace('a','hi')
#         print(s,end="")
#     else:
#         print(i,end="")


# str1 = "ansu a pillai"
# for i in str1:
#     if i=='a':
#         s=str1.replace('a','hi')
# print(s)

# list1 = ['Red','green','blue']
# n=len(list1)
# #the colors are : red, green, blue
# print("the colors are:",end="")
# s=''
# l=list1
# x=l.pop()

# for i in l:
#     # for j in range(n-1):
#         s=s+i+", "
# print(s+x)
# l=",".join(list1)
# print(f"the colors are:{', '.join(list1)}")
# print(l)


# g = "ansu is a good girl"
# b=g.split(" ")
# print(b)
# for i in b:
#     if "is" in i:
#         print(i.replace("is","hi"))
#     else:
#         print(i)


# str='My Blog'
# a=''
# for i in range(len(str)):
#     a+=str[i]
# print(a)


# Pratical questions:
# Write a Python program to get a string from a given string where all occurrences of its first char 
# have been changed to '$' except the first char itself.

# def change_char(str1):
#     char = str1[0]
#     str1 = str1.replace(char, '$')
#     str1 = char + str1[1:]
#     return str1
# print(change_char('restart'))  


# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' 
# then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

# def add_string(str1):
#     length = len(str1)
#     if length > 2:
#         if str1[-3:] == 'ing':
#             str1 += 'ly'
#         else:
#             str1 += 'ing'
#     return str1
# print(add_string('ab'))      # Output: 'ab'
# print(add_string('abc'))     # Output: 'abcing'
# print(add_string('string'))  # Output: 'stringly'


# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

# def string_both_ends(str):
#     if len(str) < 2:
#         return ''
#     return str[0:2] + str[-2:]

# print(string_both_ends('w3resource'))  # Output: 'w3ce'
# print(string_both_ends('w3'))          # Output: 'w3w3'
# print(string_both_ends('w'))           # Output: '' 



# 4, Write a Python program to count the occurrences of each word in a given sentence.
# input='the quick brown fox jumps over the lazy dog.'
# output={'the': 2, 'jumps': 1, 'brown': 1, 'lazy': 1, 'fox': 1, 'over': 1, 'quick': 1, 'dog.': 1}

# def word_count(str):
#     counts = dict()
#     words = str.split()
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#     return counts
# print( word_count('the quick brown fox jumps over the lazy dog.'))


# a="Ansu is Good Girl"
# new_string=""
# spli = a.split(" ")
# for i in spli:
#     if "Girl" in i:
#         print(i.upper())
#     else:
#         print(i)
  
# reverse a string
# stg = "hello good morning"
# reversed_string = ""
# for i in range(len(stg) - 1, -1, -1):
#     reversed_string += stg[i] + "\n"
# print(reversed_string)


# string = "hello good morning"
# print(len(string))
# for i in range(1, len(string) + 1):
#     print(string[-i])