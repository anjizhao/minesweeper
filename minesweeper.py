# ********************
# etc
# ********************


import math
import random
import string

import numpy as np


def main():
    '''the main function'''
    again = 'y'
    print('welcome to minesweeper!')
    while again == 'y' or again == 'Y':
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
        mines = create(n, m)
        solutionboard = find(mines)
        userboard = makeuserboard(mines)
        printuserboard(userboard)
        turn = 'y'
        turncount = 1
        while turn == 'y':
            turn = userturn(mines, solutionboard, userboard, m, turncount)
            turncount += 1
            print('turns: ', turncount)
            printuserboard(userboard)
        if turn == 'n':
            print('oh no, you hit a mine and died!')
        if turn == 'win':
            print('congrats, you\'ve successfully swept all the mines :D')
        again = input('play again? (y/n) ')
        if again == 'n' or again == 'N':
            if turn == 'n':
                print('remember, quitters never win! keep practicing.')
            else:
                print('goodbye, see you next time!')
    return


def userturn(mines, solutionboard, userboard, m, turncount):
    '''allow user to enter guess and update userboard.'''
    input_text = 'enter row & column of your guess (ex: ''AA''): '
    guess_str = input(input_text)
    if len(guess_str) != 2:
        print('enter two uppercase letters!')
        guess_str = input(input_text)
    letters = string.ascii_uppercase
    row = letters.index(guess_str[0])
    column = letters.index(guess_str[1])
    spacesleft = checksolution(userboard)
    print(spacesleft, ' spaces left')
    if solutionboard[row, column] != 9:
        s = str(solutionboard[row, column])
        userboard[row, column] = s
        turn = 'y'
    if spacesleft == m:
        turn = 'win'
    if solutionboard[row, column] == 9:
        for i in range(len(userboard)):
            for j in range(len(userboard)):
                if solutionboard[i, j] == 9:
                    userboard[i, j] = '*'
        turn = 'n'
    return turn


def checksolution(userboard):
    '''returns 'win' if all non-mines have been uncovered'''
    num = -1
    for i in range(len(userboard)):
        for item in userboard[i]:
            if item == 'x':
                num += 1
    return num


def makeuserboard(mines):
    '''create board that is displayed to the user.'''
    userboard = np.ones_like(mines, dtype=str)
    for i in range(len(mines)):
        for j in range(len(mines)):
            userboard[i, j] = 'x'
    return userboard


def printuserboard(userboard):
    '''given array of strings userboard, prints it without brackets'''
    letters = string.ascii_uppercase
    rowletters = '  '
    for j in range(len(userboard)):
        rowletters += letters[j]
        rowletters += ' '
    print('')
    print(rowletters)
    for i in range(len(userboard)):
        s = ''
        s += letters[i]
        s += ' '
        for item in userboard[i]:
            s += item
            s += ' '
        print(s)
    print('')


def create(n, m):
    '''creates NxN array with m mines placed randomly'''
    board = np.zeros((n, n), dtype=int)
    for i in range(m):
        pos = int(math.floor((random.random()) * (n * n)))
        if pos == n * n:
            pos = int(math.floor((random.random()) * (n * n)))
        while board.flat[pos] == 1:
            pos = int(math.floor((random.random()) * (n * n)))
        board.flat[pos] = 1
    board = board == 1
    return board


def find(mines):
    '''given boolean array, creates array with #s indicating adjacent mines'''
    solution = np.zeros(mines.shape, dtype=int)
    for i in range(len(mines)):
        for j in range(len(mines)):
            solution[i, j] = adjacent(mines, i, j)
    return solution


def adjacent(mines, i, j):
    '''given position, finds how many adjacent mines there are'''
    n = len(mines)
    number = 0
    if mines[i, j]:
        return 9
    if i > 0 and j > 0:
        if mines[i - 1, j - 1]:
            number += 1
    if i > 0:
        if mines[i - 1, j]:
            number += 1
    if i > 0 and j < (n - 1):
        if mines[i - 1, j + 1]:
            number += 1
    if j > 0:
        if mines[i, j - 1]:
            number += 1
    if j < (n - 1):
        if mines[i, j + 1]:
            number += 1
    if i < (n - 1) and j > 0:
        if mines[i + 1, j - 1]:
            number += 1
    if i < (n - 1):
        if mines[i + 1, j]:
            number += 1
    if i < (n - 1) and j < (n - 1):
        if mines[i + 1, j + 1]:
            number += 1
    return number

main()
