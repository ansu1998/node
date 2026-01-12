# Program to read list of names and sort the list in alphabetical order.

# n=int(input("Enter the number of names...."))
# names=[]
# print("Enter {} names".format(n))
# for i in range(n):
#    nam=input()
#    names.append(nam)
# names.sort()
# print(names)

   
# Program to find the sum of all even numbers in a group of n numbers entered by the user. 

n = int(input("Enter total number:"))
s=0
new_list = []
for i in range(n):
      input1 = int(input())
      new_list.append(input1)
      if new_list[i]%2==0:
        s=s+new_list[i]
print("sum is: ", s)
   

# Program to read a string and remove the given words from the string.

# string1 = input("enter your sentence: ")
# remove_str=input("removing word: ")
# words= string1.split(" ")
# s=""
# for i in words:
#     if i!=remove_str:
#         s=s+" "+i
# print(s)


# 