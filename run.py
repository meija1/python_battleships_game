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
        row, column = guess()
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


"""
Create an input function for the player to be able to
either set ships on the board and guess the opponents placed
ships.
"""


def guess():
    while True:
        try:
            row = int(input("Enter a row number: 1 - 8\n"))-1
            column = int(input("Enter a column number: 1 - 8\n"))-1
            if row in range(0, 8) and column in range(0, 8):
                return row, column
            else:
                print("Enter a valid number")
        except ValueError:
            print("Must be a number")


"""
Allow user to guess computer ship positions on the board
Check for already guessed and hit positions marking them
with spcific characters and update the hidden board.
"""


def player_turn(board):
    while True:
        row, column = guess()
        if hidden_board[row][column] == 'X' or hidden_board[row][column] == '-':
            print("It's already been hit")
        elif board[row][column] == 'X':
            hidden_board[row][column] = 'X'
            print("it's a hit!")
        else:
            print("Missed!")
            hidden_board[row][column] = '-'
        print_board(hidden_board)
        break


"""
Computer turn function selects a random spot on players board
and places the specific character depending if it already
contains them, updates and returns the players board.
"""


def comp_turn(board):
    while True:
        row = randint(0, 7)
        column = randint(0, 7)
        if board[row][column] == 'X' or board[row][column] == '-':
            row = randint(0, 7)
            column = randint(0, 7)
        elif board[row][column] == 'O':
            board[row][column] = 'X'
            print("Computer hit!")
        else:
            board[row][column] = '-'
            print("Computer missed!")
        print_board(board)
        break


"""
Function to count how many X characters is in a list
by passing the board variable trough it
and returns the total count.
"""


def check_winner(board):
    total = 0
    for x in board:
        total += x.count('X')
    return total


def play_game():
    create_ships(player_game_board)


play_game()
