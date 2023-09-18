import math
import time
from Players import HumanPlayer, ComputerPlayer


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
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
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
        # winner if 3 in a row anywhere .. we have to check all of these!
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
            diagonal1 = [self.board[i]
                         for i in [0, 4, 8]]  # left to right diagonal
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i]
                         for i in [2, 4, 6]]  # right to left diagonal
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

    letter = 'X'  # starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':  # if the letter is O, then it is the o player's turn
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        # let's define a function to make a move!
        if game.make_move(square, letter):
            # print the board if the move is valid
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')  # just empty line
            # if the game has a winner, then print the winner
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)  # pause

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    OPlayer = ComputerPlayer('O')
    XPlayer = HumanPlayer('X')
    t = TicTacToe()
    print("\nThe aim of this game is to explore adversarial search algorithms, particularly the min-max algorithm. \nIn this project, We have developed a Tic-Tac-Toe AI that employs min-max strategies to \ndetermine the optimal move at each turn, ensuring victory every time.\n")
    play(t, XPlayer, OPlayer, print_game=True)
    print("Do you want to play again? y/n")
    playAgain = input()
    if playAgain == "y":
        t = TicTacToe()
        play(t, XPlayer, OPlayer, print_game=True)
    else:
        pass
