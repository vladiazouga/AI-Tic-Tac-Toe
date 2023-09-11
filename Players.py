import math, random
"""The purpose of this file is to create the functions needed to initalize each player in the game, as well as
the ways they can interact with the gameboard. For example, a human player can only choose to select a position 
that is within the gameboard, and not currently filled with a symbol"""

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

            try:
                val = int(square)
                if val not in game.available_positions():
                    raise ValueError
                valid_square = True

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
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        alpha = -math.inf
        beta = math.inf
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # Check if the game has already finished.
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        #Maximize
        if player == max_player:
            best = {'position': None, 'score': -math.inf} 
            alpha = max(alpha, best['score'])
            #If alpha is greater than beta, that means that for minimization, the path is not needed, so it is skipped.
            if alpha >= beta:
                return best
        #Minimize
        else:
            best = {'position': None, 'score': math.inf} 
            #
            beta = min(beta, best['score'])
            #Alpha Beta pruning, if beta is less than alpha, that means it is not a path would be chosen for maximization,
            #therefore, this path is skipped.
            if beta <= alpha:
                return best

        for possible_move in state.available_positions():
            state.make_move(possible_move, player)
             # simulates a gmae to see if it is the most efficient router
            sim_score = self.minimax(state, other_player) 

            # undoes previous move to explore other possibilties
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            #If the simulated score is improved over the best score, update the best score.
            if player == max_player: 
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best