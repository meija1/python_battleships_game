# Python Battleships Game
Battleships is a python terminal game which runs in the Code Institute mock terminal on Heroku.
It's a strategic guessing game played by two players on a grid identified by letters and numbers.

This game is played on a 8 by 8 grid board with ships occupying one squere.

![responsive](https://user-images.githubusercontent.com/109754892/219420470-fa96b17b-7a9d-4556-a278-b25961360936.png)
## How to play
In this version the game asks you to place 5 ships on an 8 by 8 board.
Each time the player places ships, the game will show the players board
with ships marked as `O`. 
After they have been set the game will prompt you to enter a row
number from 1 to 8 and same for the column number. From there you will see computers board with either a miss 
`-` symbol or hit `X` symbol. The player who hits all 5 ships is the winner.
## Features
### Existing Features
* Placing ships
    * Player can place 5 ships anywhere on the board
    ![placingShips](https://user-images.githubusercontent.com/109754892/219425692-a69d1678-dd22-404f-a3d3-203d2b9dd7cb.png)
* Play against a computer
* Accepts user inputs for rows and columns
* Updates on misses and hits
    * Game shows if squere has already been guessed
    ![battleships_exampl](https://user-images.githubusercontent.com/109754892/219428213-264da177-9e21-4369-8d28-4e5bf37b8502.png)
* Input validation
    * Can only enter a number between 1 and 8
    * Cannot be a letter or text
    ![validation](https://user-images.githubusercontent.com/109754892/219428763-3210085e-1522-4f92-8e36-45589f7804a5.png)
* Shows who has won the game
### Features Left to Implement
* Allow the player to place different size ships
* Be able to select the size of the game board
* Select the games difficulty
## Data Model
The code consists mostly of functions and variables

Each function has it's own task and is being called multiple times so the code does not have to repeat and look messy. 
I tried to keep rewriting code to a minimum

Methods like `guess()` and `print_board()` are being used the most. 
Other methods are there to help create player and computer ships as well as have turns for each player and to check who has won.
## Testing
I have tested this project by doing the following:
    * Checked the code with PEP8 linter and returned no problems
    * Gave invalid inputs 
    * Tested in the local terminal and Heroku terminal
### Bugs
* All bugs were fixed with no bugs left to my knowledge
### Validator Testing
* PEP8
    * No errors were returned from PEP8
    ![python checker](https://user-images.githubusercontent.com/109754892/219438132-7585741a-faef-47e7-b2b8-042e0df99db0.png)
## Deployment
This project was deployed using Code Institute's mock terminal for Heroku
* Steps for deployment
    * Create new Heroku app
    * Set buildbacks to `Python` and `NodeJS` in order
    * Link the Heroku app to the repository
    * Click on Deploy
## Credits
* Code Institute for the deployment terminal
* Code Institute for some of the game's code
* Assigning multiple elements to list or method was taken from [StackOverflow](https://stackoverflow.com/questions/58921574/python-assign-value-to-multiple-list-elements)
* For counting number of strings in list was found here [StackOverflow](https://stackoverflow.com/questions/60120709/counting-of-elements-strings-in-list-python)
* Multi variable values was taken from here [Note](https://note.nkmk.me/en/python-multi-variables-values/)
* Most of the general bug and problem fixes was on [StackOverflow](https://stackoverflow.com/)
