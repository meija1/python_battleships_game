from random import randint

"""
Create base for 8 by 8 boards for player, computer 
and a hidden overlay one for computer.
"""
player_game_board = [[" "] * 8 for _ in range(8)]
computer_game_board = [[" "] * 8 for _ in range(8)]
hidden_board = [[" "] * 8 for _ in range(8)]

"""
Create a function to style the game board by passing a variable board
Print numbers horizontally and vertically
Finally print vertical lines and implement rows by 1
"""
def print_board(board):
    print('  1 2 3 4 5 6 7 8')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


