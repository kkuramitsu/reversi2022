import random
from reversi2022.reversi import *

class komugiAI(object):
  def name(self):
        return 'komugi077'
        
  def play(self, board, color):
    list = [
        [ 50, -20,  10,  10, -20,   50],
        [-20, -30, -10, -10, -30,  -20],
        [ 10, -10,   5,   5, -10,   10],
        [ 10, -10,   5,   5, -10,   10],
        [-20, -30, -10, -10, -30,  -20],
        [ 50, -20,  10,  10, -20,   50],
    ]
    
    s=[]
    t=[]
    for y in range(board.N):
      for x in range(board.N):
        if board.put_and_reverse(x, y, color, reverse=False) > 0:
          s.append(list[x][y])
          t.append((x, y))
          i = max(s)
          j = s.index(i)
          return t[j]
