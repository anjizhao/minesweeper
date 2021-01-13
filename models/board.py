
from itertools import chain
import random
from typing import Tuple

import numpy as np


class Board():

    def __init__(self, n, m):
        self.dim = n
        self.mine_count = m
        self.mines = np.zeros((n, n), dtype=int)  # start with no mines

    def generate(self):
        spaces = self.dim * self.dim
        # get random sample of indices to set as mines in the flattened array
        mine_indices = random.sample(range(spaces), self.mine_count)
        self.mines.flat[mine_indices] = 1

    def place_mines(self, user_first_move: Tuple[int, int]) -> None:
        # get random sample of indices to set as mines in the flattened array
        user_move_row, user_move_column = user_first_move
        user_move_index = user_move_row * self.dim + user_move_column
        spaces = list(chain(
            range(user_move_index), range(user_move_index + 1, self.dim ** 2)
        ))
        mine_indices = random.sample(spaces, self.mine_count)
        self.mines.flat[mine_indices] = 1

        return
