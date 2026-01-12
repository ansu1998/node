'''
password generator projects


The user of this random password generator will be given a random password 
after entering the number of characters, symbols, and numbers they wish to include in their password. 

Enter the number of letters in the password: 6
Enter the number of symbols in the password: 2
Enter the number of numbers in the password: 4

Generated Password: fK7&6s#9gH3j
'''


import random
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "-", 
                "{", "}", "[", "]", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("welcome to password Generator!")
n_letters= int(input("How many letters you want in your password?\n"))
n_symbols = int(input("How many symbols you want in your password?\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))
password_list =[]
for i in range(1, n_letters+1):
    char = random.choice(letters)
    password_list += char

for i in range(1, n_symbols+1):
    char = random.choice(symbols)
    password_list += char

for i in range(1, n_symbols+1):
    char = random.choice(number)
    password_list += char
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(password)