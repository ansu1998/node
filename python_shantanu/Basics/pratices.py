1, # How can you replace string space with a given character in Python?
# text = "D t C mpBl ckFrid yS le"

# text = "D t C mpBl ckFrid yS le"
# str1=""
# for i in text:
#     if i != ' ':
#         str1+=i
# print(str1)


# Given a positive integer num, write a function that returns True if num is a perfect square else False.
# This has a relatively straightforward solution. You can check if the number has a perfect square root by:

# Finding the square root of the number and converting it into an integer.
# Applying the square to the square root number and checking if it's a perfect square root.
# Returning the result as a boolean. 
# Test 1  
# We have provided number 10 to the valid_square() function. 

# By taking the square root of the number, we get 3.1622776601683795.
# By converting it into an integer, we get 3.
# Then, take the square of 3 and get 9.
# 9 is not equal to the number, so the function will return False. 

# def vaild_square(number):
#     squre = int(number**0.5)
#     if squre**2 == number:
#         print("true")
#     else:
#         print("false")
# vaild_square(25)


# Given an integer n, return the number of trailing zeroes in n factorial n!

# hints:
# To pass this challenge, you have to first calculate n factorial (n!) and 
# then calculate the number of training zeros. 

# Finding factorial 
# In the first step, we will use a while loop to iterate over the n factorial and stop when the n is equal to 1. 

# def facto():
#     number =10
#     fact=1
#     count=0
#     for i in range(1, number+1):
#         fact= fact*i
#     for j in str(fact)[::-1]:
#         if j == '0':
#             count= count+1
#         else:
#             break
#     return count
# print(facto())

# Python Program to Check if a String is Palindrome

# def palin(s):
#     if s==s[::-1]:
#         print("it is palindrom")
#     else:
#         print("it is not  palindrome")
# palin("greeka")


# # linear search
# def search1(list1, key):
#     for i in list1:
#         if i==key:
#             return "it is Found"    
#     return "it is Not Found"
# print(search1([1,2,9,6,10,7],9))


# Remove duplicate number

# arr = [10,10,20,30,30,40,40,50]
# arr1=[]
# for i in arr:
#     if i not in arr1:
#         arr1.append(i)
# print(arr1)

# count the number of word
# s= "Loin is our national animal hi"
# count=0
# new = s.split()
# for i in new:
#     count=count+1
# print(count)

# prime number 2,3,5,7 but one is not prime


# num=8
# if num==1:
#      print("it is not prime")
# else:
#     flag=0
#     for i in range(2,int(num/2)+1):
#             if num%i == 0:
#                 flag=1
#                 break
#     if flag==1:
#         print("not prime")
#     else: 
#         print("prime")

# s="aaabbbcccjb"
# for i in range(0,len(s)):
#     if s[i]==s[i+1]:
#         print(i)

# def fun(a,b):
#     return a+b
# new = fun(3,4)
# print(new)


