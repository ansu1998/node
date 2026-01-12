'''
Regrx is an expression that specifies a set of strings that matches it. 



Expression 
a+b   a*b   a-b

regex cheat sheet
https://www.rexegg.com/regex-quickstart.html

re.search(regex, string)

'''

import re

# write a python program that matches a string that has an 1 followed by zero or more 0's.

pattern=r'10*'
print(re.search(pattern, 'abc9000056718'))


# write a python program that matches a string that has an 1 followed by one or more 0's
# pattern=r'10+'
# print(re.search(pattern, 'abc0000108'))


# write a python that matches a string that has a letter followed by zero or one '0'
# pattern=r'[a-z]0?'
# print(re.search(pattern, 'a000'))

# write a python program that matches a string that has a 1 followed by 3'0's
# pattern=r'10{3}'
# print(re.search(pattern, 'tin1000'))


# write a python program to find sequence of lowercase letters joined with an_(snakecase)
# pattern = r'[a-zA-Z]+_[a-zA-Z]+'
# print(re.search(pattern, 'Python_programming'))


# check for pattern dd-mm-yyyy
# pattern=r'\d{1,2}-\d{1,2}-\d{4}'
# print(re.search(pattern, '15-12-2018'))

# find the words with exactly 8 lettersusing regex.
# pattern=r'\w{8}'
# print(re.search(pattern, 'this is an abstract'))


# sentence ending with Python
pattern=r'Python$'
# print(re.search(pattern, 'I love Python'))

print(re.search(pattern, 'I love Python\n and I love Java',re.MULTILINE))