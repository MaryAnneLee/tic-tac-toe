import math
import random

# Different type of players
class Player:
    # Letter is x or o 
    delf.letter = letter


    # All players get their next move given a game
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        # gets a random valid spot for the next move
        def get_move(self, game):
            square = random.choice(game.available_moves())

class HumanPlayer(Player):
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
                    print('Invlaid square. Try again.')
            
            return val


# The board - a single list to rep 3x3 
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] 
        self.current_winner = None  # Keeping track of the winner

    def print_board(self):
        # getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmetod
    def print_board_nums():
        # 0 | 1 | 2 etc - what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    # Available moves
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board  # show empty squares? 

    def num_empty_squares(self):
        return self.board.count(' ') # count empty spots

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. If invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False


# The moves of the game  
def play(game, x_player, o_player, print_game=True):
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
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')

        # after the move, letter needs to alternate to switch players
        letter = 'O' if letter == 'X' else 'X'

        
