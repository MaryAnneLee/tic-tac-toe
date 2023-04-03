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

        def get_move(self, game):
            pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

        def get_move(self, game):
            pass

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
