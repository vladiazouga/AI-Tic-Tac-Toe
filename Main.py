import math, time, random
#from Players import HumanPlayer, ComputerPlayer


#import math, random
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






class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        # keeps track of winner
        self.current_winner = None

    @staticmethod
    def make_board():
        # creates a 3x3 board
        return [' ' for _ in range(9)]

    # prints the board
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    # prints the board with numbers to show the positions
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # returns true if the move is valid
    def make_move(self, square, letter):
        # if the move is valid, then make the move (assign square to letter)
        # then return true. if the move is invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        #winner if 3 in a row anywhere .. we have to check all of these!
        # first let's check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False
    # returns true if there is an empty square
    def empty_squares(self):
        return ' ' in self.board
    # returns the number of empty squares
    def num_empty_squares(self):
        return self.board.count(' ')

    def available_positions(self):
        # returns a list of available positions
        return [i for i, x in enumerate(self.board) if x == " "]

# This function is the main function that runs the game. It takes in the game, the x player, 
# the o player, and a boolean that determines whether or not the game is printed.
def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O': # if the letter is O, then it is the o player's turn
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        # let's define a function to make a move!
        if game.make_move(square, letter):
            # print the board if the move is valid
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('') # just empty line
            # if the game has a winner, then print the winner
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8) # pause

    if print_game:
        print('It\'s a tie!')



if __name__ == '__main__':
    OPlayer = ComputerPlayer('O')
    XPlayer = HumanPlayer('X')
    t = TicTacToe()
    print("The aim of this game is to explore adversarial search algorithms, particularly the min-max algorithm. In this project, We have developed a Tic-Tac-Toe AI that employs min-max strategies to determine the optimal move at each turn, ensuring victory every time.")
    play(t, XPlayer, OPlayer, print_game=True)      
    print("Do you want to play again? y/n")
    playAgain = input()
    if playAgain == "y":
        t = TicTacToe()
        play(t, XPlayer, OPlayer, print_game=True)
    else:
        pass
        