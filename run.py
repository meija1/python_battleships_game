from random import randint

"""
Create base for 8 by 8 boards for player, computer 
and a hidden overlay one for computer.
"""
player_game_board = [[" "] * 8 for _ in range(8)]
computer_game_board = [[" "] * 8 for _ in range(8)]
hidden_board = [[" "] * 8 for _ in range(8)]
