
import random

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
