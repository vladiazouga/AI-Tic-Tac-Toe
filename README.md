﻿# AI-Tic-Tac-Toe
Game Components:
1.	Game Board: 3x3 grid where players place their X and O
2.	Players: One player against a computer opponent with the player deciding if they will be X or O
3.	Game Logic: Distinguishing whether the game is in progress, win, loss, or draw.
4.	User interface: Allows for the player to interact with the game.
Architecture:
1.	Main Game Loop: The central part of the game that will run until the game is over.
2.	Player Input: Records Players move and confirms them.
3.	Game Logic: Checks for wins, draws, and updates to the game.
4.	Display: Shows the game board to the console.
5.	Game State: Keeps the record of the current state of the game such as the board state and whose turn it is.
Design:
1.	Initialize game board, setting it to an empty state
2.	Display empty board to player
3.	Main game loop:
-	Prompt player for move
-	Validate move
-	Update game board with move
-	Check for a win or draw
-	Switch to CPU turn 
-	Repeat until game is over.
4.	Display the end game result (win, draw, loss)
5.	Prompt user to play again.
Data Structure:
1.	Use a 2D array to represent the game board
2.	Store the current player symbol (X or O)
3.	Define the data structures to check for win or draw.
