import math
import random
import time

# Most of the code comes from a tutorial by FreeCodeCamp.org,
# linked to in the Readme-file

# Information about the game

print("Let´s play Tic Tac Toe!\n")
print("Try to get three in a row! Vertically, horizontally or diagonally.")
print("You have the letter X and starts the game")
print("Place your move on an empty square by choosing a number between 0-8")
print("If all squares are full and no one has three in a row, it's a tie!")
print("Good luck!\n")


# Two different type of players with one base player


class Player():  # Base player
    def __init__(self, letter):
        # Letter is x or o
        self.letter = letter

    # Players get their next move given a game
    def get_move(self, game):
        pass


class HumanPlayer(Player):  # Human player
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # Checking that it is a correct value
            # If it's not a correct value, then it's invalid.
            # If the spot is not available, it's invalid.
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid input. Try again.')
        return val


class RandomComputerPlayer(Player):  # Computer player
    def __init__(self, letter):
        super().__init__(letter)
        # Gets a random valid spot for the next move

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


# The board - a single list to rep 3x3

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None  # Keeping track of the winner

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        # Getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc - what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        # If valid, then make the move (assign square to letter)
        # then return true. If invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # Function that check for a winner
    # Winner when 3 in a row horizontally, vertically or diagonally

    def winner(self, square, letter):
        # Row check
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Column check
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Diagonals check
        # The only moves possible to win a diagonal is 0,2,4,6,8
        if square % 2 == 0:
            # Left to right diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            # Right to left diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # If all checks fail
        return False

    def empty_squares(self):
        return ' ' in self.board  # Show empty squares

    def num_empty_squares(self):
        return self.board.count(' ')  # Count empty spots

    # Available moves after a move is made
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']


# The moves of the game
# Returns the winner (X or O) of the game. Or None for a tie.
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Starting letter
    # Iterate while the game still has empty squares
    while game.empty_squares():
        # Gets the move from the right player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Function on who makes a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')  # Empty line

            if game.current_winner:  # If there is a winner the game can end
                if print_game:
                    print(letter + ' wins!')
                return letter  # End the loop and exits the game

            # After one move, letter needs to alternate to switch players
            letter = 'O' if letter == 'X' else 'X'

        # Break between the moves
        time.sleep(1.8)

    if print_game:
        print("It's a tie!")

# To play the game


x_player = HumanPlayer('X')
o_player = RandomComputerPlayer('O')
t = TicTacToe()
play(t, x_player, o_player, print_game=True)
