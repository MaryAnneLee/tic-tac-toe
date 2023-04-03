import math
import random

# Three different type of players
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
        self.current_winner = None # Keeping track of the winner

    def print_board(self):
        #getting the rows
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
