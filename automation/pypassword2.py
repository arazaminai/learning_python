import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = ["!", "@","#","%","^","&","*","(","+","?","-"]

print("Welcome to PyPassword")
nr_letters = int(input("How many letters would you like?\n"))
nr_numbers = int(input("How many numebrs would you like?\n"))
nr_symbols = int(input("How many symbols would you like>\n"))

password_list = []

for i in range(nr_letters):
    password_list.append(random.choice(letters))

for i in range(nr_numbers):
    password_list.append(str(random.randint(0, 9)))

for i in range(nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for i in range(len(password_list)):
    password += password_list[i]

print(password)
