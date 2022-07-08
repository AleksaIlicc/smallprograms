import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f",
           "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nmbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ["!", "@", "#", "$", "%", "^", "&"]

password_list=[]
password=""
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

for letter in range(0,nr_letters):
    password_list.append(random.choice(letters))
for sym in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
for nmb in range(0,nr_numbers):
    password_list.append(random.choice(nmbers))

for x in range(0,len(password_list)):
    z=random.randint(0,len(password_list)-1)
    password+= password_list[z]
print(password)
