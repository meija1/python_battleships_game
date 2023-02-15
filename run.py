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

"""
Function to allow player to set 5 ships in any place on the board
Welcome message for the game, input method to place rows and columns
update the player on how many ships have been placed and return board
with the player ships on it.
"""
def create_ships(board):
    print("Welcome to Battleships Game \nPlace Your 5 ships...")
    ships = 0
    while ships < 5:
        row, column = int(input("Enter a number: 1 - 8\n"))-1
        board[row][column] = 'O'
        ships += 1
        print_board(board)
        print(f"You have placed {ships} ships")
    input("Ships set!\nPress any key to start!")
    return board


"""
Function to make computer ships on the board in random places
Computer makes 5 ships using the randint function and sets an X
in it's place if it's not been set there already, and returns the
board with the placed ships.
"""
def create_computer_ships(board):
    for ships in range(5):
        row = randint(0, 7)
        column = randint(0, 7)
        while board[row][column] == 'X':
            row = randint(0, 7)
            column = randint(0, 7)
        board[row][column] = 'X'
    return board


def play_game():
    create_ships(player_game_board)


play_game()
