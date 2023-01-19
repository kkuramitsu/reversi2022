from reversi2022.reversi import *
import random

class AI(GameAI):
    def name(self):
        return 'aki087'
    
    def play(self, board, color):
      list = [[100, -100, 5, 5, -100, 100],
              [-100, -70, 1, 1, -70, -100],
              [5, 1, 0, 0, 1, 5],
              [5, 1, 0, 0, 1, 5],
              [-100, -70, 1, 1, -70, -100],
              [100, -100, 5, 5, -100, 100]]
      while True:
        x = random.randint(0, board.N+1)
        y = random.randint(0, board.N+1)
        if board.put_and_reverse(x, y, color, reverse=False) > 0:
          return (x, y)
