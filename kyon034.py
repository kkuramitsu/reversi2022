from reversi2022.reversi import *
import random

class AI(object):
    def name(self):
        return 'kyon034'

    def play(self, board, color):
      # ランダムにおける場所を探す
      while True:
        x = random.randint(0, board.N+1)
        y = random.randint(0, board.N+1)
        if board.put_and_reverse(x, y, color, reverse=False) > 0: # とれる個数
          return (x, y)
