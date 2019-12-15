import sys

def print_board(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])

def player(): 
    while True:
        move = input()
        if move == "":
            print()
        else:
            move = int(move)
            if move in the_board.keys():
                return move
            else:
                print("Between 1-9, as shown in the diagram")

def multiplayer():
    turn = "X"
    while True:
        #break
        print("Turn for " + turn + ". Move on which space?")
        #move = input()
        move = player()
        the_board[move] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        print_board(the_board)
        if game(the_board):
            break
    
def game(board):
    if "X" in board[1] and "X" in board[2] and "X" in board[3] or "X" in board[4] and "X" in board[5] and "X" in board[6] or "X" in board[7] and "X" in board[8] and "X" in board[9]:
        print("X Wins!!!")
        return True
    if "X" in board[1] and "X" in board[4] and "X" in board[7] or "X" in board[2] and "X" in board[5] and "X" in board[8] or "X" in board[3] and "X" in board[6] and "X" in board[9]:
        print("X Wins!!!")
        return #score_x + 1
    if "X" in board[3] and "X" in board[5] and "X" in board[7] or "X" in board[1] and "X" in board[5] and "X" in board[9]:
        print("X Wins!!!")
        return #score_x + 1

    if "O" in board[1] and "O" in board[2] and "O" in board[3] or "O" in board[4] and "O" in board[5] and "O" in board[6] or "O" in board[7] and "O" in board[8] and "O" in board[9]:
        print("O Wins!!!")
        return #score_o + 1
    if "O" in board[1] and "O" in board[4] and "O" in board[7] or "O" in board[2] and "O" in board[5] and "O" in board[8] or "O" in board[3] and "O" in board[6] and "O" in board[9]:
        print("O Wins!!!")
        return #score_o + 1
    if "O" in board[3] and "O" in board[5] and "O" in board[7] or "O" in board[1] and "O" in board[5] and "O" in board[9]:
        print("O Wins!!!")
        return #score_o + 1

while True:
    the_board = {
        1: "1", 2: "2", 3: "3",
        4: "4", 5: "5", 6: "6",
        7: "7", 8: "8", 9: "9"
        }
    score_x = 0
    score_o = 0
    print_board(the_board)
    multiplayer()

    while True:
        play = input("Play again?(y/n): ")
        if play == "n":
            sys.exit()
        elif play == "y":
            break



