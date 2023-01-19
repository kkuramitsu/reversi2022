
from reversi2022.reversi import *
import numpy as np
import random

EVALUATION_BOARD = np.array([
     [45 ,  4, -1, -1,  4,  45],
    [-11 , -1, -3, -3, -1, -11],
     [ 4,  2, -1, -1,  2,  4],
 [4,  2, -1, -1,  2,   4],
    [-11, -1, -3, -3, -1, -11],
     [45,  4, -1, -1,  4, 45]])

class AI(object):
    def name(self):
        return 'Jesse084'

    def play(self, board, color):
        while True:
           idx = np.unravel_index(np.argmax(EVALUATION_BOARD), EVALUATION_BOARD.shape)
           # x = random.randint(0, board.N+1)
            #y = random.randint(0, board.N+1)
            x = idx[0]
            y = idx[1]
            if board.put_and_reverse(x, y, color, reverse=False) > 0:
                return (x, y)
