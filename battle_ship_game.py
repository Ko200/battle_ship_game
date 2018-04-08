
from random import randint
board=[]
for number in range(5):
    k=["O"]*5
    board.append(k)

def print_board(board):
    for i in board:
        print (" ".join(i))
def random_row(board):
    return randint(0,len(board)+1)
def random_col(board):
    return randint(0,len(board)+1)
ship_row=random_row(board)
ship_col=random_col(board)
print("ship_raw:",ship_row)
print("ship_col",ship_col)

for turn in range(4):
    print("Turn:\n",turn+1)
    print_board(board)
    gues_row=int(input("guess row:  \n"))
    gues_col=int(input("guess column:   \n"))
    if gues_row==ship_row and gues_col==ship_col:
        print("Congratulation!... You sink the ship\n")
        break
    else:
        if gues_row not in range(5) or gues_col not in range(5):
            print("Oops.. the ship is not even in the ocean\n")
        elif board[gues_row][gues_col]=="x":
            print("You guessed the one already\n")
        else:
            print("You missed the battle shp\n")
            board[gues_row][gues_col]='x'
        if turn==3:
            print("Game Over !\n")
            print_board(board)
