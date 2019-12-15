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

def game():
    

while True:
    the_board = {
        1: "1", 2: "2", 3: "3",
        4: "4", 5: "5", 6: "6",
        7: "7", 8: "8", 9: "9"
        }
    score_x = 0
    score_y = 0
    turn = "X"

    for i in range(9):
        #break
        print_board(the_board)
        print("Turn for " + turn + ". Move on which space?")
        #move = input()
        move = player()
        the_board[move] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    
    print_board(the_board)

    while True:
        play = input("Play again?(y/n): ")
        if play == "n":
            sys.exit()
        elif play == "y":
            break




