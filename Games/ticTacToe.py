import sys
import random

# The board grid
def print_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])

# Sets the winner
def win(board):
    if "X" in board[1] and "X" in board[2] and "X" in board[3] or "X" in board[4] and "X" in board[5] and "X" in board[6] or "X" in board[7] and "X" in board[8] and "X" in board[9]:
        print("X Wins!!!")
        return True
    elif "X" in board[1] and "X" in board[4] and "X" in board[7] or "X" in board[2] and "X" in board[5] and "X" in board[8] or "X" in board[3] and "X" in board[6] and "X" in board[9]:
        print("X Wins!!!")
        return True
    elif "X" in board[3] and "X" in board[5] and "X" in board[7] or "X" in board[1] and "X" in board[5] and "X" in board[9]:
        print("X Wins!!!")
        return True

    elif "O" in board[1] and "O" in board[2] and "O" in board[3] or "O" in board[4] and "O" in board[5] and "O" in board[6] or "O" in board[7] and "O" in board[8] and "O" in board[9]:
        print("O Wins!!!")
        return True
    elif "O" in board[1] and "O" in board[4] and "O" in board[7] or "O" in board[2] and "O" in board[5] and "O" in board[8] or "O" in board[3] and "O" in board[6] and "O" in board[9]:
        print("O Wins!!!")
        return True
    elif "O" in board[3] and "O" in board[5] and "O" in board[7] or "O" in board[1] and "O" in board[5] and "O" in board[9]:
        print("O Wins!!!")
        return True

def bot(played, turn):
    while True:
        bot = random.randint(1, 9)
        if bot not in played:
            played.append(bot)
            break
    return bot


# Move validation
def player(turn, played):
    while True:
        try:
            move = input()
            if move != "":  #(1) prevents empty string to int error
                move = int(move)
                if move in the_board.keys(): #(2) checks if the move played isn't too high or low
                    if move not in played: #(3) Prevents overide of values
                        played.append(move)
                        return move
                    else: #(3)
                        print_board(the_board)
                        print("Error: Space already taken")
                        print("Turn for " + turn + ". Move on which space?")
                else: #(2)
                    print_board(the_board)
                    print("Error: Only between 1-9, as shown in the diagram")
                    print("Turn for " + turn + ". Move on which space?")
            else: #(1)
                print_board(the_board)
                print("Turn for " + turn + ". Move on which space?")
        except ValueError:
            print_board(the_board)
            print("Error: Only whole-numbers betweem 1-9, as shown in the diagram")
            print("Turn for " + turn + ". Move on which space?")

# 2 player game
def multiplayer(played):
    turn = "X"
    
    for i in range(10):
        if i == 9:
            print("Donkey Game")
            break
        print("Turn for " + turn + ". Move on which space?")
        
        if turn == "X":
            move = player(turn, played)
            the_board[move] = turn
            turn = "O"
        else:
            move = bot(played, turn)
            the_board[move] = turn
            turn = "X"
        
        print_board(the_board)

        if win(the_board):
            break




# The front end
while True:
    try:
        the_board = {
            7: "7", 8: "8", 9: "9",
            4: "4", 5: "5", 6: "6",
            1: "1", 2: "2", 3: "3"
            }
        turns_played = []

        print_board(the_board)
        multiplayer(turns_played)

        while True:
            play = input("Play again?(y/n): ")
            
            if play == "n":
                sys.exit()
            elif play == "y" or play == "":
                break
    except KeyboardInterrupt:
        sys.exit()
