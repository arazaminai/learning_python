#ROCK PAPER SCISSORS
from sys import exit
from os import system
import time
import random




def player():
    move = input("Enter your move: (r)ock (p)aper (s)cissors (q)uit \n").lower()
    if move == "r": 
        print("ROCK versus...")
        return move
    elif move == "p":
        print("PAPER verus...")
        return move
    elif move == "s":
        print("SCISSORS versus...")
        return move
    elif move == "q":
        exit()
    else:
        print("ERROR: Invalid character!")
        player()

def bot():
    npc = random.randint(1, 3)
    if npc == 1:
        npc = "r"
        print("Rock")
        return npc
    elif npc == 2:
        npc = "p"
        print("PAPER")
        return npc
    else:
        npc = "s"
        print("SCISSORS")
        return npc

def score(move, npc):
    global ties
    global wins
    global loses
    ties = 0
    wins = 0
    loses = 0
    #Tie
    if npc == move:
        ties += 1
        print("It's A Tie!")
        return ties
    #Wins
    elif player == "r" and npc == "s": 
        wins += 1
        print("You Win!")
    elif player == "p" and npc == "r":
        wins += 1
        print("You Win!")
    elif player == "s" and npc == "p":
        wins += 1
        print("You Win!")
        return wins
    #Loses
    elif (player == "s" and npc == "r") or (player == "r" and npc == "p") or (player == "p" and npc == "s"):
        loses += 1
        print("You Lose!")
        #return loses




while True:
    print("ROCK PAPER SCISSORS\n"
          "%s Wins, %s loses, %s ties" % (wins, loses, ties))
    move = player()
    npc = bot()
    score(move, npc)


