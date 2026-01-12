# list is  a datatype , use to store multiple item in a single variable
# list1 = ['ansu',3,'sanju',True]
# print(list1)
# list1 = [1,2,3,4,5,"ansu","ansu",True,"sanju"]
# print(list1)

# list2 = ["ansu", 25, "erkm"]
# print(list2)

# # index
# print(list1[-2])

# print(list1[0:8:2])

# start 0  end 7  step 0+2, 3+2


# mylist = ['apple','orange','banana',7,8.9,9000]
# print(mylist)

# mylist = [1,2,3,4,5,"ansu","sanju",8.9,9.8]
# print(mylist[1])
# print(len(mylist))


lst = ['red','green','orange', 'blue','black',8,9.9]
# print(lst[-1])

# # print(lst[-1])

# # # # slice
# print(lst[0:5])
# print(lst[0:])
# print(lst[3:])
# print(lst[:3])
# print(lst[:])
# print(lst[4:7])
# print(lst[::-1])
# print(lst[-4:-2])
# print(lst[-1::-1])

'''
-2 = 
'''
# print(lst[::-1])

lst = ['red','green','orange','blue']
print(len(lst))


lst[3] = 'violet'
print(lst)

# iterat this list using for loop and while


# list1 = [5,7,9,10]
# for i in range(0, len(list1)):
#     print(list1[i])

# i=0
# while i<len(list1):
#     print(list1[i])
#     i=i+1

# i=len(list1)-1
# while i>=0:
#     print(list1[i])
#     i=i-1

# for i in list1:
#     print(i)

# lst = ['red','green','orange','blue']
# i=0
# while i<len(lst):
#     print(lst[i])
#     i=i+1


# lst = ['red','green','orange','blue']
# i = 0
# while i < len(lst):
#     print(lst[i])
#     i = i + 1


# lst = ['red','green','orange','blue']
# for i in lst:
#     print(i)

# for i in range(0,len(lst)):
#     print(lst[i])


# # + operator
# lst_2 = [1, 'two', 3, 'four']
# lst_3 = ['pen', 'book']
# lst_4 = lst_2 + lst_3
# print(lst_4)

# lst_4 = lst_2*2 + lst_3*3
# print(lst_4)

# lst_1 = ['one','two','three','four','five','one','one','six']
# lst_2 = [22,10,25,30,99,55]
# print(max(lst_1))
# print(min(lst_1))
# print(max(lst_2))
# print(min(lst_2))

# # # append

# lst_1 = ['red','green','orange','blue']
# lst_1.append('seven')
# lst_1.append('eight')
# print(lst_1)


# # # # # count
# lst_1 = ['one','two','two','four','five','six']
# print(lst_1.count('two'))


# # insert
# lst_1 = ['one','two','three','four','one','one','six']
# lst_1.insert(2, 'seven')
# print(lst_1)
# # # insert(index, value)

# # pop
# lst_1 = ['one','two','three','four','one','one','six']
# val = lst_1.pop()
# val = lst_1.pop(1)
# print(val)
# print(lst_1)


# del lst_1
# print(lst_1)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# # # lst_2 = [5,9,8,1,0,3]

# # # Remove
# lst = ['two','two','one','three','four']
# lst1=[]
# for i in lst:
#     if i != 'two':
#         lst1.append(i)
# print(lst1)

# lst.remove('two')
# lst.remove('two')
# print(lst)


# lst = [67,90,21,76]
# lst = ['two','two','one','three','four']
# lst.sort()
# print(lst)



# # # reverse
# lst.reverse()
# print(lst)

# sum of the list list=[1,2,3] o/p=6
# list1 = [1,2,3,4,5]
# sum1=0
# for i in list1:
#     sum1 = sum1+i
#     avg= sum1/len(list1)
# print(avg)
# print(sum1)


# sum1=0+1 =1 1+2=3  3+3=6

# list=[6,8,9,9,9,5,5,1]
# # [6,8,9,5,1]

# sum=0
# for i in list:
#     sum = sum+i
# print(sum)



# lst = [67,90,21,76,94]
# for i in range(len(lst)-1,-1,-1):
#     print(lst[i])


# print even word 
#  example=
# i/p: s= 'Hi i am ansu'
# o/p : hi am ansu


# s='Hi i am ansu'
# list2 =[]
# s1 = s.split(' ')
# for i in s1:
#     if len(i)%2 ==0:
#         list2.append(i)
# print(list2)



# 1,program to maximum value in a list
# 2,Find sum and average of List in Python
#3, Write a Python program to remove duplicates from a list. 

# 1,program to maximum value in a list

# lst = [67,90,21,76,94]
# lst.sort()
# print(lst[-1])


lst = [67,90,100,21,76]
index1=lst[0]
for i in lst:
    if i<index1:
        index1=i
print(index1)


    
# practies
# q1,Find sum and average of List in Python
# list1 = [1,2,3,4,5]
# sum1 =0
# for i in list1:
#     sum1 = sum1+i
#     avg = sum1/len(list1)
# print('sum is ',sum1)
# print('avg  is',avg)  





'''
Write a Python program to remove duplicates from a list. 
# '''

# a = [10,20,20,10,50,60,40,80,50,40]
# uniq_items = []
# for x in a:
#     if x not in uniq_items:
#         uniq_items.append(x)
# print(uniq_items)

# program to add odd numbers  in a list --Excercise
# q5, double the elements in list


# program to add odd numbers  in a list 
list2= [1,2,3,4,5]
sum1 =0
for i in list2:
    if i%2==1:
        sum1= sum1+i
print(sum1)




# a = [1,3,5,7,9,11]
# list3=[]
# for i in a:
#     i=i*2
#     list3.append(i)
# print(list3)


# d = [i*2 for i in a]
# print(d)



# print(30+20*3**2)



# Input list
# write a python program to count a value from specified index  in a list ?
# lst = [10, 20, 30, 10, 40, 50]
# value = int(input("Enter the value to count: "))
# index = int(input("Enter the index to start counting from: "))
# count = sum(1 for x in lst[index:] if x == value)
# print(f"Number of occurrences of {value} from index {index}: {count}")



# lst = [10, 20, 30, 10, 40, 50,10]
# count = 0
# value = int(input("Enter the value to count: "))
# index = int(input("Enter the index to start counting from: "))
# for i in range(index, len(lst)):
#     if lst[i] == value:
#         count += 1
# print("Number of occurrences of value",count)

 




# . Write a Python program to print a specified list after removing the 0th,
# 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']



# my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# new_list = []
# for index, value in enumerate(my_list):
#     if index not in [0, 4, 5]:
#         new_list.append(value)
# print(new_list)


# lst = ['one','two','one','three','two','four','one']

# lst_1 = ['one','two','three','four','one','one']
# new_lst = []
# for item in lst_1:
#     if item != 'one':
#         new_lst.append(item)
# print(new_lst)

# list = [1,2,3,4,5,6]
# sum=0
# new_list = []
# for i in list:
#     if i%2==0:
#         new_list.append(i)
#         sum= sum+i
# print(new_list)
# print("sum is :",sum)


# lst_1 = ['one','two','three','four','one','one']
# index = 0
# while index < len(lst_1):
#     if lst_1[index] == 'one':
#         lst_1.remove('one')
#     else:
#         index += 1
# print(lst_1)
    

