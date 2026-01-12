# {key:vaule}
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and  do not duplicate values
# 

# dictn = {'name':'Ansu', 'age':25, 'address': 'erkm'}
# print(dictn)


# print(dictn["name"])
# print(dictn["age"])

# print(dictn.get("name"))
# print(dictn.get("age"))

# dictn = {'a':'apple','b':'bat','c':'cat','d':'doll','e':'ten'}
# print(dictn)

# print(dictn[0])

# print(dictn['a'])

# print(dictn['e'])
# print(dictn.get("c"))

# change the value
# dictn = {'a':'apple','b':'bat','c':'cat','d':'doll','e':'ten'}
# print(dictn)

# dictn['a'] = "ant"
# print(dictn)

# dictn['b'] = 3
# print(dictn)

# dictn['g'] = "gun"
# print(dictn)

# dictn['k']="ket"
# print(dictn)

dictn = {'a':'apple','b':'bat','c':'cat','d':'doll','e':'ten'}
print(dictn)

# dictn.update({"e": 2020})
# dictn.update({"h": 2021})
# print(dictn)


# dictn = {'a':'apple','b':'bat','c':'cat','d':'doll','e':'ten'}
# del dictn['d']
# del dictn["c"]
# print(dictn)

# dictn.pop("e")
# print(dictn)

# dictn.popitem()
# print(dictn)

# del dictn
# print(dictn)

# dictn.clear()
# print(dictn)


dictn = {'a':'Apple','b':'bat','c':'cat','d':'doll'}
# print(dictn.values())

# print(dictn.keys())

# print(dictn.items())

# for i in dictn:
#     print(i)
#     print(dictn[i])
#     # print(dictn.get(i))
#    



# diction={'a':100, 'b':200, 'c':300}

# keys: a, values: apple
# dictn.clear()
# print(dictn)


# pratices
# iteration using while loop


# iteration of values

# dictn = {'a':'Apple','b':'bat','c':'cat','d':'doll'}
# for k in  dictn.values():
#     print('values:',k)

# # # # iteration of keys
# dictn = {'a':'Apple','b':'bat','c':'cat','d':'doll'}
# for v in dictn.keys():
#     print('keys: ',v)

# dictn = {'a':'Apple','b':'bat','c':'cat','d':'doll'}
# for v,n in dictn.items():
#     print(v,n)

# iteration of keys and values
# key a values apple

# dictn = {'a':'Apple','b':'bat','c':'cat','d':'doll'}
# for k,v in dictn.items():
#     print('key: ',k, 'values: ',v)


# dictn = {'a':'Apple','b':'bat','c':'cat','d':'doll'}
# new = list(dictn)
# i=0
# while i < len(new):
#     # print(new[i])
#     print(dictn[new[i]])
#     i=i+1

# input myDict = {'a': 100, 'b': 200, 'c': 300}
# # output= adding values 100+200+300 =600   




# myDict = {'a': 100, 'b': 200, 'c': 300}
# sum1 =0
# for i in myDict:
#     sum1=sum1+myDict[i]
#     print(sum1)


# f = sum(myDict.values())
# print(f)


# input1= {1:2,2:3,5:9}
# output'{2: 1, 3: 2, 9: 5}


mydict = {1:2,2:3,5:9}
rev_dict = {}
for i in mydict:
    val = mydict[i]
    rev_dict[val] = i
print(rev_dict)




mydict = {1:2,2:3,5:9}
rev_dict = dict()
for i,k in mydict.items():
    rev_dict[k] = i
print(rev_dict)



# lst = [1,2,3]
# lst_2d = [[1,2,3],[4,5,6],[7,8,9]]

# print(lst_2d[0][0])
#     # print(lst[0])
# print(lst_2d[0][1])

# for i in lst_2d:
#     print(i)



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


# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
#  If the string length is less than 2, return the empty string instead.

# Sample String : 'ansuapillai'
# Expected Result : 'anai'
# Sample String : 'an'
# Expected Result : 'anan'
# Sample String : ' 'a'
# Expected Result : Empty String


# def string_both_ends(str):
#   if len(str) < 2:
#     return ''

#   return str[0:2] + str[-2:]

# print(string_both_ends('ansuapillai'))
# print(string_both_ends('an'))
# print(string_both_ends('a'))





# The original string is : geekforgeeks best for geeks
# "best" = "good and better", "geeks" = "all CS aspirants"
# Replaced Strings : geekforgeeks good and better for all CS aspirants





# Python3 code to demonstrate working of
# Replace words from Dictionary
# Using split() + join() + get()



# test_str = 'geekforgeeks best for geeks'
# print("The original string is : " + str(test_str))
# lookp_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}
# temp = test_str.split()
# print(temp)
# res = []
# for wrd in temp:
# 	print(wrd)
# 	res.append(lookp_dict.get(wrd, wrd))
# 	print(res)	
# res = ' '.join(res)
# print("Replaced Strings : " + str(res))


# for i in range(1,11):
#     print(i)



