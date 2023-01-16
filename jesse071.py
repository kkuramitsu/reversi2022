from reversi2022.jesse071 import *
import random
class jesse071AI(object):
    def name(self):
        return 'jesse071'

    def play(self, board, color):
      while True:
        x = random.randint(0, board.N+1)
        y = random.randint(0, board.N+1)
        if board.put_and_reverse(x, y, color, reverse=False) > 0:
          return (x, y)
