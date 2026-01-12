'''
Write a Python program to sum all the items in a list. 
'''

# list_1 = [2,3,4,5]
# sum=0
# for i in list_1:
#     sum= sum+i
# print(sum)


# sum=0
# for i in range(0,8):
#     sum = sum+i
# print(sum)

# Write a Python program to multiply all the items in a list.

# list_0 = [3,5,6,7,8]
# mul=1
# for i in list_0:
#     mul=mul*i
# print(mul)


'''
 Write a Python program to get the largest number from a list. 
'''

# list_0 = [3,5,61,7,8]
# n=list_0[0]
# for i in list_0:
#     if i>n:
#         n=i
# print(n)


'''
 Write a Python program to get the smallest number from a list.
'''

# list_0 = [3,5,61,7,0,8]
# n=list_0[0]
# for i in list_0:
#     if i<n:
#         n=i
# print(n)


'''
program to count the number of strings where the string length is 2 or more and 
the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

list_0 = ['abc', 'xyz', 'aba', '1221','cbc']
count=0
for i in list_0:
    if len(i)>=2 and i[0]==i[-1]:
        count=count+1
        # print(i)
print(count)

'''
 Write a Python program to remove duplicates from a list.
'''

list_0=['abc', 'xyz', 'aba', 'abc','1221','cbc']
list_new=[]
for i in list_0:
    if i not in list_new:
        list_new.append(i)
print(list_new)

# def list_0(list_0):
#   list_new=[]
#   for i in list_0:
#       if i not in list_new:
#           list_new.append(i)
#   print(list_new)

# s=[9,8,8,7,3,7,8,0,1]
# list_0(s)


'''
Write a Python program to check a list is empty or not.
'''



# list_1=[1,2,3]
# if list_1==[]:
#     print('Empty list')
# else:
#     print('not empty')


# n="This is a python language"
# s=n.split(" ")
# for i in s:
#     if len(i)%2==0:
# 	    print(i)



'''
-+
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead of the empty string. 
Sample String : 'ecconomy'
Expected Result : 'ecmy'
Sample String : 'ec'
Expected Result : 'ecec'
Sample String : ' 'e'
Expected Result : Empty String
'''


# def string_both_ends(str):
#   if len(str) < 2:
#     return ''

#   return str[0:2] + str[-2:]

# print(string_both_ends('w3resource'))
# print(string_both_ends('w3'))
# print(string_both_ends('w'))

# def greatest(a):
#     if(len(a)>2):
#         print( a[0:2]+a[-2:])
#     elif(len(a)==2):
#         print( a*2)
#     else:
#       print("empty string")
# a=input("enter input")
# greatest(a)


# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# List_1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']



# Gaming coding quiz 

# print("Welcome to my Computer Quiz! ")
# playing = input("Do you want to play? ")

# # if playing.lower() != "yes":
# #     quit()
# if playing == "yes" or "YES":
#     print("Okay! Let's play! :")

#     score=0
#     answer = input("Is the coding language python, named after  a snake? ")
#     if answer=="no":
#         print("Correct! ")
#         score += 1
#     else:
#         print("In Correct")


#     answer = input("what does cpu stands for ?")
#     if answer=="central processing unit":
#         print("Correct! ")
#         score += 1
#     else:
#         print("In Correct")

#     answer = input("what does gpu stands for ?")
#     if answer=="graphics processing unit":
#         print("Correct! ")
#         score += 1
#     else:
#         print("In Correct")


#     answer = input("what does RAM stands for ?")
#     if answer=="random access memory":
#         print("Correct! ")
#         score += 1
#     else:
#         print("In Correct")

#     print("You got ", score , " question correct !")
#     print("You got ", (score/4*100) , "% .")




# Python program to print odd Numbers in a List

# list1 = [10, 21, 4, 45, 66, 93]
# list3=[]
# for num in list1:
#     if num % 2 != 0:
#         list3.append(num)
# print(list3)


# Python: Convert a list of characters into a string

# s = ['a', 'b', 'c', 'd']
# str1 = ''.join(s)
# print(str1)


# 26/7/2024
# # Write a Python program to get the frequency of the elements in a list.

random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
frequency = {}

for item in random_list:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1
print(frequency)


# 5. program to count the number of strings where
# the string length is 2 or more and the first and last character
# are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2



# my_list = ['abc', 'xyz', 'aba', '1221']
# counter = 0
# for i in my_list:
#     if len(i) >= 2:
#         if i[0] == i[len(i)-1]: # or if i[0] == i[-1]:
#             counter += 1
# print(counter)


# Write a Python program to check a list is empty or not


# my_list = []

# if my_list:
#     print('list is not empty')
# else:
#     print('list is empty')

# 10. Write a Python program to find the list of words that are longer
# than n from a given list of words.

# def is_longer(words, n):
#     long_words = []
#     for word in words:
#         if len(word) > n:
#             long_words.append(word)
#     return long_words


# my_list = ['cat', 'dog', 'apple', 'table', 'bags']

# print(is_longer(my_list, 4))

"""
# 11. Write a Python function that takes two lists and returns True
# if they have at least one common member.
"""

# list_one = [1, 2, 3, 4]
# list_two = [8, 9, 10, 11]

# def common_member(li1, li2):
#     for i in li1:
#         if i in li2:
#             return True
#         return False

# print(common_member(list_one, list_two))


"""
9. Write a Python program to find the repeated items of a tuple.
"""

# my_tuple = (1, 1, 2, 3, 4, 4, 5)

# repeated_items = []
# for i in my_tuple:
#     if my_tuple.count(i) > 1:
#         if i not in repeated_items:
#             repeated_items.append(i)
# print(repeated_items)

"""

21. Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary. 
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output: 
ac
ad
bc
bd
"""

# my_dict = {'1':['a','b'], '2':['c','d']}

# my_list = list(my_dict.values())
# for i in my_list[0]:
#     for j in range(1, len(my_list)):
#         for x in my_list[j]:
#             my_string = i + x
#             print(my_string)





# https://github.com/silvuple/w3resource.com-python-exercises/blob/master/lists_exercises_python.py

# link for program using function

"""

12. Write a Python program to print a specified list after removing the 0th,
4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

"""


# my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# new_list = []
# for index, value in enumerate(my_list):
#     if index not in [0, 4, 5]:
#         new_list.append(value)
# print(new_list)


# Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. This 
# enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.

# enumerate(iterable, start=0)

# l1 = ["eat", "sleep", "repeat"]
# s1 = "geek"
  
# # obj1 = enumerate(l1)
# obj2 = enumerate(s1)
  
# # print ("Return type:", type(obj1))
# print (list(enumerate(l1)))
  
# # changing start index to 2 from 0
# print (list(enumerate(s1, 2)))



"""
7. Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'poor' follows the 'not', replace
the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'
"""

# my_string = input("enter a string ")

# # solution 1
# not_position = my_string.find('not')
# poor_position = my_string.find('poor')

# if not_position < poor_position and not_position != -1:
#     new_string = my_string[:not_position] + 'good' + my_string[poor_position+4:]
# else:
#     new_string = my_string

# print(new_string)



# Write a Python program to concatenate elements of a list.


# color = ['red', 'green', 'orange']

# red-green-orange                                                                                              
# redgreenorange

# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
 
#     i += 1


# color = ['red', 'green', 'orange']
# print('-'.join(color))
# print(''.join(color))


# dictn= {}
# j=0
# set1= {"tomato","ginger","cabbage","potato"}
# for i in set1:   
#     dictn[j]=i
#     j=j+1

# print(dictn)



# take a input n and return the sum of n number from 0 to n

# def sum_num(n):
#     sum=0
#     for i in range(n+1):
#         sum = sum+i
#     return sum
# print(sum_num(5))



# input1= ['G','()','(al)']
# for i in input1:
#     if i == '()':
#         print('o')
#     if i =='(al)':
#         print()



# name = input('Enter File:')
# handle = open(name, 'r')
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0)+1
#     print(counts)

# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word 
#         bigcount = count

# print(bigcount,bigword)



'''
input will gives like 7564168

example separate odd place integers: 5,4,6

you have to return a 4 digit OTP by squareing the digits.


digits from above example: 5,4,6

square of those numbers: 25,16,36

so the otp to be returned is first four digits: 2516

# '''
# 7564168
# num = input("Enter a numbers: ")
# len_num = len(num)
# otp =""
# for i in range(1,len_num,2):
#     odd = int(num[i])
#     odd1 = odd**2
#     otp+=str(odd1)
# print(otp[0:4])




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

Take input from user in the give format (consist of name and code),

find max digit from Code which is less or equal to the length of string

and put that place char in final string, if there is no any digit 
found which not satisfy the condition that simply put 'X'


# input: Abhishek:43848, Mayur:3749, yeah: 7878

# output:kueX
'''



# inp = input("enter a name: ")
# code = int(input("enter a code"))
# for i in inp:
#     for j in code
#     if max(code <= len(inp):





# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made
#  by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
 


# # 8, Write a Python program to count the number of characters (character frequency) in a string. 
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
#     return dict
# print(char_frequency('google.com'))




# str1='google.com'
# dict = {}
# for n in str1:
#     keys = dict.keys()
#     if n in keys:
#         dict[n] += 1
#     else:
#         dict[n] = 1
# print(dict)





# Write a Python program to get a single string from two given strings, separated by a space and 
# swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


# def chars_mix_up(a, b):
#   new_a = b[:2] + a[2:]
#   new_b = a[:2] + b[2:]

#   return new_a + ' ' + new_b
# print(chars_mix_up('abc', 'xyz'))



'''
Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.

string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}

'''

# def letter_combinations(digits):
#     if digits == "":
#         return []
#     string_maps = {
#         "1": "abc",
#         "2": "def",
#         "3": "ghi",
#         "4": "jkl",
#         "5": "mno",
#         "6": "pqrs",
#         "7": "tuv",
#         "8": "wxy",
#         "9": "z"
#     }
#     result = [""]
#     for num in digits:
#         temp = []
#         for an in result:
#             for char in string_maps[num]:
#                 temp.append(an + char)
#         result = temp
#     return result

# digit_string = "47"
# print(letter_combinations(digit_string))
# digit_string = "29"
# print(letter_combinations(digit_string))



'''

write a python program to get a string made of the first 2 and the last 2 char from a given a string .
if the string length is less than 2, return empty string.

a= "aa"
output="aaaa"


a="python"
output="pyon"


a="a"
output="empty string"

'''

# string1 = "pythons"
# if len(string1)>=2:
#     print(string1[0:2]+string1[-2:])
# elif len(string1)==2:
#     print(string1*string1)
# else:
#     print("Empty strings")


'''

x="In linguistics and grammar, a sentence is a linguistic expression, such as the English example
 "The quick brown fox jumps over the lazy dog." In traditional grammar it is typically defined as a
string of words that expresses a complete thought, 
 or as a unit consisting of a subject and predicate.
 " python program to how to get  "grammar it is typically defined" from string?
'''
# x = 'In linguistics and grammar, a sentence is a linguistic expression, such as the English example "The quick brown fox jumps over the lazy dog." In traditional grammar it is typically defined as a string of words that expresses a complete thought, or as a unit consisting of a subject and predicate.'

# start_index = x.index("grammar it is typically defined")  # Find the starting index of the desired phrase
# end_index = start_index + len("grammar it is typically defined")  # Calculate the ending index

# desired_phrase = x[start_index:end_index]  # Extract the desired phrase from the string

# print(desired_phrase)



'''
Write a Python function that takes a list of words and return the longest word and 
the length of the longest one.
'''

# words_list=["PHP", "Exercises", "Backend"]
# word_len = []
# for n in words_list:
#     word_len.append((len(n), n))
# word_len.sort()
# print(word_len)
# print('word length',word_len[-1][0]) 
# print('Longest word: ',word_len[-1][1])


# words_list=["PHP", "Exercises", "Backend"]
# len1=len(words_list)
# new=words_list[0]
# list1=[]
# for i in words_list:
#     if len(i)>len(new):
#         new=i
#         list1.append(new)
# print(list1)


# def fibanocci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     elif(n<0):
#         return "Error"
#     elif(n==1):
#         return 1
#     else:
#         return fibanocci(n-1)+fibanocci(n-2)
    
# n=int(input("Enter a number: "))
# fib = fibanocci(n)
# print(fib)
    


# list1 = ["ansu","sara","sanju"]
# for i in list1:
#     print(i)

# for i in range(0,len(list1)):
#     print(list1[i])

# i=0
# while i<len(list1):
#     print(list1[i])
#     i=i+1





# ****
# **
# *****
# *
# ******

# list1 = [4,2,5,1,6]
# for i in list1:
#     print(i*'*')



# Write a Python 
# function that takes a list of words and return the longest word and  
# the length of the longest one. 

# a = ["one", "two", "third", "four"]
# max1 = len(a[0])
# temp = a[0]
# for i in a:
#     if(len(i) > max1):

#         max1 = len(i)
#         temp = i

# print("The word with the longest length is:", temp,
#     " and length is ", max1)


# Fibanoicc seriers

# def Fibonacci(n):
# 	if n < 0:
# 		print("Incorrect input")

# 	elif n == 0:
# 		return 0

# 	elif n == 1 or n == 2:
# 		return 1

# 	else:
# 		return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(6))

# 1 1 2 3 5 8 13 21 34 55 89 

# Gaming rock paper scissors


# import random

# options = ("rock", "paper", "scissors")
# running = True

# while running:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")

#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False

# print("Thanks for playing!")


# Write a Python program to find the maximum and minimum values in a set.

# setn = {5, 10, 3, 15, 2, 20}
# print("Original set elements:")
# print(setn)
# print(type(setn))
# print("\nMaximum value of the said set:")
# print(max(setn))
# print("\nMinimum value of the said set:")
# print(min(setn)) 


# 16. Write a Python program to generate and print a list of first
# and last 5 elements where the values are square of numbers between
# 1 and 30 (both included).


# my_list = [x**2 for x in range(1,31)]
# print(my_list[:5],my_list[-5:])