import math, random
"""The intention behind this file is to establish the necessary functions 
for initializing each player in the game, along with defining their interactions with the game board. 
For instance, a human player can exclusively opt for positions within the game board that are both valid and unoccupied by symbols."""

class Player():

    #When this function is called, assigns the player the letter that is passed
    def __init__(self, letter):
        self.letter = letter

    #Placeholder as this function is defined in other player types
    def get_move(self, game):
        pass

#Inherits traits from Player class
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    #Function gets the input of the human players move, checks if it is valid, and returns the position if it is valid
    def get_move(self, game):
        valid_square = False
        val = None

        #While valid_square is false
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move 0 - 9: ')
            #Checks if the input is an integer, and if it is within the gameboard

            try:
                val = int(square)
                #Checks if the input is within the gameboard
                if val not in game.available_positions():
                    raise ValueError
                valid_square = True #If the input is valid, set valid_square to true

            except ValueError:
                print('Input Invalid')

        return val

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = None
        #Computer starts off randomly if the game has just started.
        if len(game.available_positions()) == 9:
            square = random.choice(game.available_positions())
        #If the game has already begun, optimize the computers strategy.
        else:
            #Gets the best move for the computer
            square = self.minimax(game, self.letter)['position']
        return square
    #Minimax algorithm, which is a recursive algorithm that simulates a game to see if it is the most efficient router
    def minimax(self, state, player):

        alpha = -math.inf #Alpha is the best score that the maximizer can achieve
        beta = math.inf #Beta is the best score that the minimizer can achieve
        max_player = self.letter #Max player is the computer
        other_player = 'O' if player == 'X' else 'X'

        # Check if the game has already finished.
        # first, check if the previous move was a winner
        # this is our base case
        if state.current_winner == other_player:
            # we should return position AND score because we need to keep track of the score
            # for minimax to work
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        #Maximize
        #initialize some dictionaries to keep track of the best score and position
        if player == max_player:
            best = {'position': None, 'score': -math.inf} #each score should maximize (be larger)
            alpha = max(alpha, best['score'])
            #If alpha is greater than beta, that means that for minimization, the path is not needed, so it is skipped.
            if alpha >= beta:
                return best
        #Minimize
        else:
            best = {'position': None, 'score': math.inf} #each score should minimize (be smaller)
            #
            beta = min(beta, best['score'])
            #Alpha Beta pruning, if beta is less than alpha, that means it is not a path would be chosen for maximization,
            #therefore, this path is skipped.
            if beta <= alpha:
                return best

        for possible_move in state.available_positions():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
             # simulates a gmae to see if it is the most efficient router
            sim_score = self.minimax(state, other_player) 

            # undoes previous move to explore other possibilties
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            # step 4: update the dictionaries if necessary
            #If the simulated score is improved over the best score, update the best score.
            if player == max_player: 
                if sim_score['score'] > best['score']:
                    best = sim_score #replace best
            else: # but minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best