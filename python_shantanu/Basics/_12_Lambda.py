# Anonymous function(lambda)

#  lambda function can take any number of arguments, 
# but can only have one expression. 

# As this is a single-line syntax, the function is much more readable. 
# There’s no need to search for the argument on another line.


# # Syntax
# # lambda arguments: expression

#  1

# def square2(a):
#     print(a*a)
# square2(2)


# x= lambda a: a*a
# print(x(2))

# x= lambda a,b,c,d: a+b+c+d 
# print(x(2,4,5,6))

# 1,pratices add two number

# def add(a,b):
#     return a + b
# print(add(3,4))

 # Output: 7


# s = lambda a,b,c: a+b
# print(s(3,5,7))


# 2, pratice smallest of two numbers

def smallnum(a,b):
    if a<b:
        return a
    else:
        return b
print(smallnum(10,11))


s = lambda a,b:a if a<b else b
print(s(13,10))


# # used in function
def myfun(n):
    return lambda a:a-n

mydouble = myfun(2)
print(mydouble(11))



# def myfun(n):
#     return lambda a: a-n

# mydouble = myfun(2)
# mytripler = myfun(3)

# print(mydouble(11))
# print(mytripler(110))


# program lambda in function  

input=[1,2,3,4,5]
output = [0.5, 1.0, 1.5, 2.0, 2.5]


list1 = [1,2,3,4,5]
list2 = []
for i in list1:
    list2.append(i /2)
print(list2)
  

# s= lambda lst: [i/2 for i in lst]
# print(s([1,2,3,4,5]))

# s = lambda lst: [i / 2 for i in lst if i % 2 == 0]
# print(s([1, 2, 3, 4, 5]))

# list1 = [1,2,3,4,5]
# list2 = []
# for i in list1:
#     f = lambda i: i /2
#     list2.append(f(i))
# print(list2)

# s = lambda lst: [i / 2 for sublist in lst for i in sublist if i % 2 == 0]
# print(s([[1, 2, 3], [4, 5, 6]])) 

# map, filter, sum, reversed, enumerate, sorted

# home work

# 4, print even number in a list using lambda

# list2= [1,2,3,4,5]
# new=[]
# for i in list2:
#     if i%2 ==0:
#         new.append(i)
# print(new)

# f= filter(lambda x:x%2==0, list2)
# print(list(f))


# def add(a, b):
#     return (lambda x, y: x + y)(a, b)

# print(add(3, 4)) 