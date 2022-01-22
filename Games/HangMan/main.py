#HangMan
import random as rand
from os import system

def stringanise(letters):
    str_letters = ""
    for i in range(len(chosen_word)):
        str_letters += letters[i]
    return str_letters

def add_letters(letters, inputs): 
    for i in range(len(chosen_word)):
        if inputs == chosen_word[i]:
            letters[i] = inputs

def match():
    for i in range(len(letters)):
        print("")
        

def clear():
    system("cls||clear")

dictionary = open("english.txt", "r")
line = dictionary.read().split("\n")
dictionary.close()

for key, value in enumerate(line):
    if len(value) < 3:
        line.remove(value)
        continue
    for i in range(len(value)):
        if value[i] in [".", "'"]:
            line.remove(value)

chosen_word = rand.choice(line)
letters = []

from art import logo
print(logo)

for i in range(len(chosen_word)):
    letters.append(" _")

lives = 6
turns = []
from art import stages

while True:
    if not(" _" in letters):
        print(stages[lives])
        print("you win!")
        break
    if lives == 0:
        print(f"you lose the word is {stringanise(chosen_word)}")
        break
    inputs = input(f"{stringanise(letters)}\n Guess a letter: ")
    print(stages[lives])
    add_letters(letters, inputs)
    if not(inputs in chosen_word) and not(inputs in turns):
        lives -= 1 
    if inputs in turns:
        print("Letter has been used, please try again")
    turns.append(inputs)
