from reversi2022.reversi import*
import random

class AI(object):
    def name(self):
        return 'mm030'

    def play(self, board, color):
      evalution_board = [[10, -5, 5, 5, -5, 10],
                        [-5, -8, 1, 1, -8, -5],
                        [5, 1, 0, 0, 1, 5],
                        [5, 1, 0, 0, 1, 5],
                        [-5, -8, 1, 1, -8, -5],
                        [10, -5, 5, 5, -5, 10]]
      while True:
        x = random.randint(0, board.N+1)
        y = random.randint(0, board.N+1)
        if board.put_and_reverse(x, y, color, reverse=False) > 0:
          return (x, y)
