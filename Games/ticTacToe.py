the_board = {
        "top-L": " ", "top-M": " ", "top-R": " ",
        "mid-L": " ", "mid-M": " ", "mid-R": " ",
        "bot-L": " ", "bot-M": " ", "bot-R": " "
        }

def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid_M"] + "|" + board["mid-M"])
    print("-+-+-")
    print(board["bot-L"] + "|" + board["bot-M"] + "|" + board["bot-L"])

print_board(the_board)
