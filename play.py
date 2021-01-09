
from models import Board, Game


def play():
    again = True
    print('welcome to minesweeper!')
    while again:
        game = Game()
        game.play()

        again_input = input('play again? (y/n) ')
        if again_input in ('n', 'N'):
            again = False

    print('goodbye')

play()
