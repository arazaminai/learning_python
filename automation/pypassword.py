#Pypassword - password generator
from random import randint as rand

def alphabet():
    letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    letters.sort()
    caps = []

    for i in range(len(letters)):
        caps.append(letters[i].upper())
    
    letters.extend(caps)
    return letters

def main(nr_letters, nr_numbers, nr_symbols):
    let_arr = []
    let_string = ""

    for i in range(nr_letters):
        let_arr.append(letters[rand(0, len(letters) - 1)])

    for i in range(nr_numbers):
        let_arr.insert(rand(0, len(letters) - 1), str(rand(0, 9) ))
        

    for i in range(nr_symbols):
        let_arr.insert(rand(0, len(letters) - 1), symbols[rand(0, len(symbols) -1)])

    for key, value in enumerate(let_arr):
        let_string += value
    
    return let_string

letters = alphabet()
symbols = ["!","@","#","$","%","^","&","*","(",")","+"]

print("Welcome to the Pypassword Generator!")
nr_letters = int(input("How many letters you would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

print(main(nr_letters, nr_numbers, nr_symbols))