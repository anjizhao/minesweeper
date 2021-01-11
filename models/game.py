
from models import Board

class Game():

    def __init__(self):
        self.board = None
        self.solutionboard = None
        self.userboard = None

    def _create_board(self):
        n_input = ''
        m_input = ''
        while not (n_input.isdigit() and m_input.isdigit()):
            if n_input or m_input:
                print('you must input integers.')
            n_input = input('choose what dimension square board you want: ')
            m_input = input('how many mines? ')
        print('good luck!!')
        n = int(n_input)
        m = int(m_input)

        self.board = Board(n, m)

    def start(self):
        self._create_board()
        self.board.generate()
        print(self.board.mines)

    def play(self):
        self.start()
