import random, sys

wins = 0
losses = 0
ties = 0
tries = 0
print("ROCK, PAPER, SCISSORS")

while True:
    print(str(wins) + " Wins, " + str(losses) + " Losses, " + str(ties) + "Ties")
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player = input()
        if player == "q":
            print("Scared of a computer! XD")
            sys.exit()
        elif player == "r" or player == "p" or player == "s":
            break
        else:
            print("ERROR 404: Players brain not found!!!")

    if player == "r":
        print("ROCK versus...")
    elif player == "p":
        print("PAPER versus..,")
    else:
        print("SCISSORS versus...")


    npc = random.randint(1, 3)
    if npc == 1:
        npc = "r"
        print("ROCK")
    elif npc == 2:
        npc = "p"
        print("PAPER")
    elif npc == 3:
        npc = "s"
        print("SCISSORS")

    if player == npc:
        ties += 1
        print("It's a tie!")
    #losses
    elif player == "r" and npc =="p":
        losses += 1
        print("You lose!")
    elif player == "p" and npc =="s":
        losses += 1
        print("You lose!")
    elif player == "s" and npc =="r":
        losses += 1
        print("You lose!")
    #wins
    elif player == "p" and npc =="r":
        wins += 1
        print("You win!")
    elif player == "s" and npc =="p":
        wins += 1
        print("You win!")
    elif player == "r" and npc =="s":
        wins += 1
        print("You win!")

    if wins == 2 or losses == 2:
        break

if wins == 2:
    print("Don't get happy, it's just a computer")
else:
    print("You lose! Good luck in the robot uprising, you'll need it! ;)")
