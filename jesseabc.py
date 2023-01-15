from .reversi import *

class AI(GameAI):
  def name(self):
    return 'Jesse123'

  def play(self, board, color):
    for y in range(board.N):
      for x in range(board.N):
        if board.put_and_reverse(x, y, color):
          return(x, y)
