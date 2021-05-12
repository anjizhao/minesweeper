
import string
from typing import Tuple

from models import Board

class Game():

    def __init__(self):
        self.board = None

    def _create_board(self):
        n_input = ''
        m_input = ''
        while not n_input.isdigit() or int(n_input) < 2 or int(n_input) > 26:
            if n_input:
                if not n_input.isdigit():
                    print('you must input an integer.')
                else:
                    print('board size must be between 2-26.')
            n_input = input('choose square board dimension (2-26): ')
        n = int(n_input)
        while not m_input.isdigit() or int(m_input) >= n * n:
            if m_input:
                if not m_input.isdigit():
                    print('you must input an integer.')
                elif m_input:
                    print('too many mines (there are {} spots).'.format(n * n))
            m_input = input('how many mines? ')
        m = int(m_input)

        print('good luck!!')

        self.board = Board(n, m)

    def start(self):
        # self._create_board()  # generates empty board (no mines)

        self.board = Board(10, 5)  # temp for testing

        # the user should never hit a mine on the first move.
        # place mines _after_ their first guess
        user_move = self.get_user_move()
        self.board.place_mines(user_move)
        # after the mines are placed, actually play the user's move
        self.do_user_move(user_move)
        print(self.board.solution)
        self.board.print_solution()
        self.board.print_user_board()

    @classmethod
    def _valid_move_input(cls, input_str: str):
        if len(input_str) != 2:
            print('must enter two uppercase letters')
            return False
        return True

    @classmethod
    def get_user_move(cls) -> Tuple[int, int]:
        input_text = 'enter row & column of your guess (ex: "AA"): '
        guess_str = ''
        while not cls._valid_move_input(guess_str):
            guess_str = input(input_text)
        letters = string.ascii_uppercase
        row = letters.index(guess_str[0])
        column = letters.index(guess_str[1])
        return (row, column)

    def do_user_move(self, move: Tuple[int, int]):
        self.board.user_move(move)
        return

    def play(self):
        self.start()
