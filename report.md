# Overview / Report

_Emmanuel David_

This project aimed to implement the min-max algorithm with alpha-beta pruning in a tic-tac-toe game, creating an unbeatable machine opponent. To briefly summarize, min-max is an adversarial search algorithm that, in this specific implementation, navigates a tree of possible plays in the tic-tac-toe game and evaluates the advantages resulting from choosing a particular set of moves. A simulated game with a higher rating signifies a greater advantage for the computer player, whereas a lower "min" rating favors the enemy player. Alpha-beta pruning is a modification to the min-max algorithm that significantly speeds up the runtime by eliminating the need to search irrelevant branches, comparing them to the current min and max paths explored.

### Design (Giovanni Smith)

In crafting our code, Giovanni drew heavily from Kylie Ying's Tic Tac Toe solution. This was mainly due to trouble visualizing the creation of a tic-tac-toe board in a terminal environment, as we all were more familiar with creating game boards in languages like HTML and CSS.

One significant challenge he faced during development was understanding the algorithm. None of us, including Vladia and myself, had much experience with searching algorithms beyond BFS and DFS. To overcome this, Giovanni turned to external resources, including tutorials like the one by Sebastian Lague on alpha-beta pruning.

### Coding (Vladia Zouga)

On top of the source code, Vladia added comments to explain each piece of the function. This greatly aided in our understanding of the program, as we could always reference them when needed. 

After the implementation of alpha-beta pruning in the program, she noticed an increase in response times during each of the computer's turns. The longest response time was less than 1000ms and occurred primarily at the beginning of the game when the human player went first. This is because, at the start of the game, there are more possible moves to be made. As a result, the algorithm takes slightly longer to go through and choose the most efficient route.

Future improvements that could be added to the project include:

- Implementation in a webpage using TypeScript, leveraging our existing experience in creating an AI tic-tac-toe project in TypeScript.
- Introducing a score system to keep track of wins.
- Adding a reset button to allow players to restart a game that is already in progress.
- Adding a button that allows players to undo a move they made.
- Incorporating animations to create a more interactive game, potentially implemented with GUI styling.

### Screenshots / Documentation

Additionally, the screenshots displaying the fully functioning program can be found inside the GitHub repository, labeled Game1.png and Game2.png.

The first screenshot showcases a normal game between the player and the algorithm, where the computer predictably wins. Basic game functionality is displayed. The human user can interact and place their symbol on the board by choosing a number that represents an open spot on the board. Any number outside the bounds of the game throws an error. Each turn is correctly labeled for the player, a victory is displayed at the end of each game, and a prompt asks if the player wants to play again. In the case that the player chooses to input a character outside the binary "y/n", the program simply registers it as an "n" and ends the game.
