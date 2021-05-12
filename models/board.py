
from itertools import chain
import random
import string
from typing import List, Tuple

import numpy as np


class Board():

    def __init__(self, n, m):
        self.dim: int = n
        self.mine_count: int = m

        # mine locations (indices in flattened board array)
        self.mine_indices: List[int]

        # solution board
        self.solution = np.zeros((n, n), dtype=int)  # start with no mines

        # mask of what tiles the user has uncovered
        self.user_board_mask = np.zeros((n, n), dtype=int)

    def place_mines(self, user_first_move: Tuple[int, int]) -> None:
        # get random sample of indices to set as mines in the flattened array
        # mines can go anywhere except for the user's first move tile
        user_move_index = self._flatten_cell_index(user_first_move)
        spaces = list(chain(
            range(user_move_index), range(user_move_index + 1, self.dim ** 2)
        ))
        self.mine_indices = random.sample(spaces, self.mine_count)

        # calculate each cell's surrounding mine count, populate solution board
        self._solve()

        # print(self.mine_indices)
        # print([self._unflatten_cell_index(m) for m in self.mine_indices])
        return

    def _flatten_cell_index(self, t: Tuple[int, int]) -> int:
        row, col = t
        return row * self.dim + col

    def _unflatten_cell_index(self, i: int) -> Tuple[int, int]:
        row = i // self.dim
        col = i - (row * self.dim)
        return (row, col)

    def _get_adjacent_tiles(self, t: Tuple[int, int]) -> List[Tuple[int, int]]:
        # return list of all the tiles around `t` (up to 8)
        row, col = t
        adj = []

        for r_offset in [-1, 0, 1]:
            if 0 <= (row + r_offset) < self.dim:
                for c_offset in [-1, 0, 1]:
                    if 0 <= (col + c_offset) < self.dim:
                        if (r_offset, c_offset) != (0, 0):
                            # don't include this tile
                            adj.append((row + r_offset, col + c_offset))

        return adj


    def _solve(self):
        # fill in solution board
        # for each mine, add 1 to the count of each of its surrounding cells
        for m in self.mine_indices:
            t = self._unflatten_cell_index(m)
            for a in self._get_adjacent_tiles((t)):
                self.solution[a] += 1

        # then, mark each of the actual mines as -1
        self.solution.flat[self.mine_indices] = -1

        return

    @staticmethod
    def _display_tile(tile: int) -> str:
        if tile < 0:
            return '*'
        if tile == 0:
            return '.'
        return str(tile)

    def _stringify_board(self):
        x = np.array([
            np.array([self._display_tile(t) for t in row])
            for row in self.solution
        ])
        return x

    def _stringify_user_board(self):
        y = np.zeros_like(self.user_board_mask, dtype=str)
        y[:] = 'x'
        for coords in zip(*np.where(self.user_board_mask)):
            y[coords] = self._display_tile(self.solution[coords])
        return y

    def user_move(self, move: Tuple[int, int]):
        self.user_board_mask[move] = 1


    def print_board(self, board):
        letters = string.ascii_uppercase
        print('  {}'.format(' '.join(letters[:self.dim])))
        for i in range(self.dim):
            print('{} {}'.format(
                letters[i],
                ' '.join(board[i]),
            ))


    def print_solution(self):
        self.print_board(self._stringify_board())
        return


    def print_user_board(self):
        self.print_board(self._stringify_user_board())
        return

