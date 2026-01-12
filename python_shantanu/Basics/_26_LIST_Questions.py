'''
Write a Python program to remove duplicates from a list. 
'''

# a = [10,20,20,10,50,60,40,80,50,40]
# uniq_items = []
# for x in a:
#     if x not in uniq_items:
#         uniq_items.append(x)
#         print(uniq_items)




# python program to count the occurence of an element in a list ?
# mylist = [15,6,7,10,12,10,20,28,10]

# x=10
# output=3

# mylist = [15,6,7,10,12,10,12,28,10]
# num = int(input("enter a number: "))
# for i in mylist:
#     if num==i:
#         t=mylist.count(i)
# print(t)


# def function1(list1,n2):
#     for i in list1:
#         if n2==i:
#             return list1.count(i)
    
# n2=int(input("Enter a number: "))
# print(function1([15,6,7,10,12,10,12,28,10],n2))


# try:
#     a=int(input("enter a number1: "))
#     b=int(input("enter a number2: "))
#     print(a+b)
# except:
#     print(" it would be handle")
# else:
#     print("Good Bye")

def myfun():
    a=10
    b=20
    def inner():
        print("just print")

        

@myfun
def fun2():
    print("additional function")

myfun()
