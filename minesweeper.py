# ********************
# etc
# ********************

import numpy as np
import random
import string
import math

def main():
    '''the main function'''
    again = 'y'
    print 'welcome to minesweeper!'
    while again == 'y' or again == 'Y':
        N = input('choose what dimension square board you want: ')
        m = input('how many mines? ')
        print 'good luck!!' 
        mines = create(N,m)
        solutionboard = find(mines)
        userboard = makeuserboard(mines)
        printuserboard(userboard)
        turn = 'y'
        turncount = 1
        while turn == 'y':
            turn = userturn(mines, solutionboard, userboard, N, m, turncount)
            turncount += 1
            print 'turns: ', turncount
            printuserboard(userboard)
        if turn == 'n':
            print 'oh no, you hit a mine and died!'
        if turn == 'win':
            print 'congrats, you\'ve successfully swept all the mines :D'
        again = raw_input('play again? (y/n) ')
        if again == 'n' or again = 'N':
            if turn == 'n':
                print 'remember, quitters never win! keep practicing.'
            else:
                print 'goodbye, see you next time!'
    return

def userturn(mines, solutionboard, userboard, N, m, turncount):
    '''allow user to enter guess and update userboard.'''
    input_text = 'enter row & column of your guess (ex: ''AA''): '
    guess_str = raw_input(input_text)
    if len(guess_str) != 2:
        print 'enter two uppercase letters!'
        guess_str = raw_input(input_text)
    letters = string.ascii_uppercase
    column = letters.index(guess_str[0])
    row = letters.index(guess_str[1])
    spacesleft = checksolution(userboard)
    print spacesleft, ' spaces left'
    if solutionboard[column, row] != 9:
        s = str(solutionboard[column, row])
        userboard[column, row] = s
        turn = 'y'
    if spacesleft == m:
        turn = 'win'
    if solutionboard[column, row] == 9:
        for i in range(len(userboard)):
            for j in range(len(userboard)):
                if solutionboard[i,j] == 9:
                    userboard[i,j] = '*'
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
    userboard = np.ones_like(mines, 'S')
    for i in range(len(mines)):
        for j in range(len(mines)):
            userboard[i,j] = 'x'
    return userboard

def printuserboard(userboard):
    '''given array of strings userboard, prints it without brackets'''
    letters = string.ascii_uppercase
    rowletters = '  '
    for j in range(len(userboard)):
        rowletters += letters[j]
        rowletters += ' '
    print ''
    print rowletters
    for i in range(len(userboard)):
        s = ''
        s += letters[i]
        s += ' '
        for item in userboard[i]:
            s += item
            s += ' ' 
        print s
    print ''

def create(N,m):
    '''creates NxN array with m mines placed randomly'''
    board = np.zeros((N,N), dtype = int)
    for i in range(m):
        pos = int(math.floor((random.random())*(N*N)))
        if pos == N*N:
            pos = int(math.floor((random.random())*(N*N)))
        while board.flat[pos]==1:
            pos = int(math.floor((random.random())*(N*N)))
        board.flat[pos] = 1
    board = board == 1
    return board

def find(mines):
    '''given boolean array, creates array with #s indicating adjacent mines'''
    solution = np.zeros(mines.shape, dtype = int)
    for i in range(len(mines)):
        for j in range(len(mines)):
            solution[i,j] = adjacent(mines, i, j)
    return solution

def adjacent(mines, i, j):
    '''given position, finds how many adjacent mines there are'''
    n = len(mines)
    number = 0
    if mines[i,j] == True:
        return 9
    if i>0 and j>0:
        if mines[i-1, j-1] == True:
            number += 1
    if i>0: 
        if mines[i-1, j] == True:
            number += 1
    if i>0 and j<(n-1):
        if mines[i-1, j+1] == True:
            number += 1
    if j>0:
        if mines[i, j-1] == True:
            number += 1
    if j<(n-1):
        if mines[i, j+1] == True:
            number += 1
    if i<(n-1) and j>0:
        if mines[i+1, j-1] == True:
            number += 1
    if i<(n-1):
        if mines[i+1, j] == True:
            number += 1
    if i<(n-1) and j<(n-1):
        if mines[i+1, j+1] == True:
            number += 1
    return number 

main()
