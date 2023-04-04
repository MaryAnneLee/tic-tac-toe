import math
import random
import time

# Different type of players

class Player():  # Base player
    def __init__(self, letter):
        # Letter is x or o
        self.letter = letter

    # All players get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):  # Computer player
    def __init__(self, letter):
        super().__init__(letter)
        # gets a random valid spot for the next move
        def get_move(self, game):
            square = random.choice(game.available_moves())
            return square

class HumanPlayer(Player):  # Human player
    def __init__(self, letter):
        super().__init__(letter)

        def get_move(self, game):
            valid_square = False
            val = None
            while not valid_square:
                square = input(self.letter + '\'s turn. Input move (0-9):')
                # Checking that this is a correct value by trying to cast
                # it to an integer, and if it's not, then we says its invalid.
                # if that spot is not available on the board, we also say its invalid
                try:
                    val = int(square)
                    if val not in game.available_moves():
                        raise ValueError
                    valid_square = True
                except ValueError:
                    print('Invalid square. Try again.')
            
            return val


# The board - a single list to rep 3x3

class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # Keeping track of the winner

    def print_board(self):
        # getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc - what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # Available moves after a move is made
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board  # show empty squares? 

    def num_empty_squares(self):
        return self.board.count(' ')  # count empty spots

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. If invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    # Function that check for a winner

    def winner(self, square, letter):
        # winner when 3 in a row horisontal, vertical or diagonal
        # row check
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # column check
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # diagonals check
        # the only moves possible to win a diagonal is 0,2,4,6,8
        if square % 2 == 0:
            # left to right diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            # right to left diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # if all checks fail
        return False


# The moves of the game  
def play(game, x_player, o_player, print_game=True):
    # Returns the winner (the letter) of the game. Or None for a tie.
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        # gets the move from the right player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # defines function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to {square}')
                game.print_board()
                print('')  # just empty line
            
            if game.current_winner:  # If there is a winner the game can end
                if print_game:
                    print(letter + ' wins!')
                return letter  # IN THE WRONG PLACE? 

        # after the move, letter needs to alternate to switch players
        letter = 'O' if letter == 'X' else 'X'

    # break between tha moves
    time.sleep(8.8)

    if print_game:
        print("It's a tie!")

# play the game


if __name__ == ' __main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
