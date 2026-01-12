# Python break is used to terminate the execution of the loop. 

# Loop{
#     Condition:
#         break
#     }

 
# for i in range(10): 
#     if i == 7: 
#         break
#     else:
#         print(i)


# num = 0
# for i in range(10): 
# 	num =num+1
# 	if num == 8: 
# 		break
# 	print("The num has value:", num) 
# print("Out of loop") 

# i=0 num=1
# i=1  num=2
# i=2 num=3
# i=4 num=4
# ''
# i=7

# Python Continue
# Python Continue Statement skips the execution of the program block after the continue statement
# and forces the control to start the next iteration.

# Syntax


# for i in range(10): 
#     if i == 7: 
#         continue
#     else:
#         print(i) 

# x=0
# while x<=10:
#     if x == 6:
#         x=x+1
#         continue
#     print(x)
#     x+=1

# for var in "Geeksforgeeks":
# 	if var == "e":
# 		continue
# 	print(var, end="")


# pass

# for var in "Geeksforgeeks":
# 	if var == "e":
# 		pass
		
	
# i=1
# while True:
#     if i%3==0:
#         break
#     print(i)
#     i+=1


# What will be the output of the following Python code?

# x = 'abcd'
# for i in x:
#     print(i)
#     x.upper()

# a) a B C D
# b) a b c d
# c) A B C D
# d) error



# x = 'abcd'
# for i in x:
#     print(i.upper())

# a) a b c d
# b) A B C D
# c) a B C D
# d) error



# x = 'abcd'
# for i in range(x):
#     print(i)

#  a) a b c d
# b) 0 1 2 3
# c) error
# d) none of the mentioned   



# x = 'abcd'
# for i in range(len(x)):
#     print(i)

# a) a b c d
# b) 0 1 2 3
# c) error
# d) 1 2 3 4



# x = 'abcd'
# for i in range(len(x)):
#     print(i.upper())

# a) a b c d
# b) 0 1 2 3
# c) error
# d) 1 2 3 4



# x = 'abcd'
# for i in range(len(x)):
#     i.upper()
# print(x)


# a) a b c d
# b) 0 1 2 3
# c) error
# d) none of the mentioned



# x = 'abcd'
# for i in range(len(x)):
#     x[i].upper()
# print(x)

# a) abcd
# b) ABCD
# c) error
# d) none of the mentioned



# x = 'abcd'
# for i in range(len(x)):
#     x = 'a'
#     print(x)

# a) a
# b) abcd abcd abcd
# c) a a a a
# d) none of the mentioned




# x = 'abcd'
# for i in range(len(x)):
#     print(x)
#     x = 'a'


# a) a
# b) abcd a a a
# c) a a a a
# d) none of the mentioned



# print(4+3%5)

# **arg
# s = "ansu"
# print(s.split("n"))