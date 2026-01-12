# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, changeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# # Duplicates Not Allowed

# set1 = {"Tomato","carrot","cabbage",45,57}
# print(set1)

# # not 
# print(set1[0])


# set1 = {'apple','orange'}
# x= list(set1)
# x[0]='violet'
# # x.append("grapes")
# y= set(x)
# print(y)



# set1 = {"Tomato","carrot","cabbage",45,57,"onion"}
# set1.add("potato")
# set1.add("onions")
# print(set1)

# # print("Tomato" in set1)

# print(len(set1))

# # # update
# # Duplicates Not Allowed
# set1 = {"Tomato","carrot","cabbage",45,57,"onion"}
# set1.update(["onion","onion","chilli","potato"])
# set1.update(["hi"])
# print(set1)


# # remove
# set1 = {"Tomato","carrot","cabbage","onion",89}
# set1.remove(89)
# print(set1)

# set1.discard("onions")
# print(set1)

# set1 = {"Tomato","carrot","cabbage","onion"}
# set2 = {1,2,3,4}
# set3 = set1.union(set2)
# print(set3)

# # # # not working
# # print(set1+set2)

# # # # clear
# set1 = {"Tomato","carrot","cabbage",45,57}
# set1.clear()
# print(set1)

# del-delete

# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

# set1= {"tomato","ginger","cabbage","potato"}
# del set1
# print(set1)



# set1= {"tomato","ginger","cabbage","potato"}
# for i in set1:
#     print(i) 

# set1 = {"tomato","ginger","cabbage","potato"}
# list1 = list(set1)
# for x in range(0,len(list1)):
#     print(list1[x])
    
# my_set = {"tomato","ginger","cabbage","potato"}
# my_list = list(my_set)
# i = 0
# while i < len(my_set):
#     print(my_list[i])
#     i += 1

# pratices
# input1={"tomato","ginger","cabbage","potato"}
# # output={0: 'ginger', 1: 'potato', 2: 'tomato', 3: 'cabbage'}


# dict1={}
# count=0
# for i in input1:
#     dict1[count] = i
#     count = count+1
# print(dict1)








# input1= {"tomato","ginger","cabbage","potato"}
# dict1 ={}
# count=0
# for i in input1:
#     dict1[count] = i 
#     count = count+1
# print(dict1)





    














