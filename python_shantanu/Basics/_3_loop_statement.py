# for loop
# while loop

'''
while condition:
    statment
    increment/decrement
 
# '''
# print 1 to 10

# i = 10
# while i>=1:
#     print(i)
#     i=i-1



# program to print 50 to 100
# program to print 10 to 1


# i=1
# while i<=10:
#     print("hello",i)
#     i=i+1


# i =10
# while i>=1:
#     print(i)
#     i = i-1


# i=10
# while  i>=1:
#     print(i)
#     i=i-1

# i=10
# while i>=1:
#     print(i)
#     i=i-2

# i=0
# while i<=10:
#     print(i)
#     i=i+2
    
# i=1
# while i<=10:
#     print(i)
#     i=i+1

# print 10 to 1 using while loop


# i = 10
# while i>=0:
#     print(i)
#     i = i-1

# print('loop completed')


# for loop

'''

for variable  in iteratable:
    statment

    range(start, stop, step)
'''

# print 1 to 10  10 = n+1
# for i in range(1,13):
#     print(i)

# for i in range(0, 13):
#     print(i)


# for i in range(0,11,2):
#     print(i)


# for i in range(1,51):
#     print("hello")
    

# for i in range(12,0,-1):
#     print(i)

# i=1
# for i in range(1,12):
#     if i==6:
#         print("hello")
#     else:
#         print(i)

# 1
# 2
# 3
# 4
# 5
# hello
# 7
# 8
# 9
# 10
# for i in range(1,11):
#     if i==6:
#         print("hello")
#     else:
#         print(i)

    
# 5! = 5*4*3*2*1

# for i in range(1,11):
#     if i==6:
#         print("hello")
#     else:
#         print(i)


    
# for i in range(12,0,-1):
#     print(i)
     
        
# i = int(input("Enter the limit:"))
# for i in range(0, i+1, 2):
#     print(i)

#Calculate the product of numbers from 1 to 5.
# Calculate the sum of squares of numbers from 1 to 5.
# Calculate the product of squares of numbers from 1 to 5.



#  Calculate the sum of numbers from 1 to 5.
# s=0
# for i in range(1,6):
#     s=s+i
#     print(s)


# factorial of a given number-5!-5*4*3*2*1
# sum of n natural numbers

# Calculate the sum of numbers from 1 to 5.
# 

# Counting Characters: Count the number of occurrences of a specific character in a string.
# Printing a Pattern: Print a triangle pattern.
# reverse of a given number 123-321


# num=5
# sum1=1
# for i in range(1,num+1):
#     sum1=sum1*i
#     print(sum1)

# Sum of natural numbers up to num
# 5 = 5+4+3+2+1
# 5!=5*4*3*2*1=120

# sum=1
# num=5
# for i in range(1,num+1):
#     sum=sum*i
# print('sum os n natural number:',sum)


'''
i=0 sum=0+0=0
i=1 sum=0+1=1
i=2 sum=1+2=3
i=3 sum=3+3=6
i=4 sum=6+4=10
i=5 sum=10+5=15

'''

# num = 5
# sum=  0
# while(num>0):
#     sum=sum+num
#     num=num-1
#     print("sum is",sum)


'''
num=5 sum=0+5=5 
num=4 sum= 5+4=9
num=3  sum=9+3=12`          
num=2 sum=12+2=14
num=1 sum=14+1=15


'''
# Calculate the sum of squares of numbers from 1 to 5.
# sum = 0
# for i in range(1,6):
#     sum = sum+i**2
# print(sum)


# Counting Characters: Count the number of occurrences of a specific character in a string.

# string = "hello"
# char_to_count = input("enter a character from string : ")
# count = 0
# for char in string:
#     if char == char_to_count:
#         count = count+1
# print("Number of occurrences of", char_to_count, "in", string, "is", count)

# Printing a Pattern: Print a triangle pattern.
'''
*
**
***
****
*****
'''
# for i in range(1,6):
#     print("*"*i)


# for i in range(1,6):
#     print('*'*i)


# range(start, stop, step)
# factorial of number
'''
5!=5*4*3*2*1
'''

# num = int(input("enter a number: "))
# factorial = 1
# if num<0:
#     print("less than zero have no factorial")
# elif num ==0:
#     print('Factorial is one')
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#         print(factorial)

# for i in range(1,11):
#     print(i)



'''
i=1 fact=1*1=1
i=2 fact = 1*2=2
i=3 fact = 2*3=6
i=.......
...


# reverse of a number 1234---4321
# '''

# num = 1234
# revese_num = 0
# while num != 0:
#     digit = num%10
#     revese_num= revese_num*10+digit
#     num //= 10
# print(revese_num)


'''
digit= 1234%10 = 4
revers_num = 0*10+4 = 4
num = 123

 digit = 123%10 = 3
 revese_num = 43
 num=12

 digit = 2
 revese_num = 432
 num = 1

 digit = 1
 reve=4321
 num = 0
'''


# Python program to check if the number is an Armstrong number or not
# 1^3 + 5^3 + 3^3 = 153

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   print(digit)
   sum =sum+ digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")





# Write a program that takes a list of numbers and returns a new list containing only the prime numbers.

# A prime number is a natural number greater than 1 that cannot be formed by multiplying two 
# smaller natural numbers. 
# In other words, a prime number is a number that is only divisible by 1 and itself.

# For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they cannot be divided evenly by any 
# other number except 1 and themselves.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime_numbers = []

# for num in numbers:
#     if num > 1:
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#         if is_prime:
#             prime_numbers.append(num)

# print("Prime numbers:", prime_numbers)






# string = "hello good morning"
# for i in range(1, len(string) + 1):
#     print(string[-i])













