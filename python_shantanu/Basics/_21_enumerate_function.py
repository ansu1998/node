# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.

# enumerate(iterable, start=0)

fruits_list = ['apple','orange','banana','watermelon','grapes']
# for i in range(len(fruits_list)):
#     print(i,fruits_list[i])

for pos, fruits in enumerate(fruits_list):
    print(pos, fruits)

# for pos, fruits in enumerate(fruits_list,3):
#     print(pos, fruits)

for pos, fruits in enumerate('fruits_list',1):
    print(pos, fruits)


fruits_list = ['apple','orange','banana','watermelon','grapes']
fruit_enum = enumerate(fruits_list)
print(dict(fruit_enum))


