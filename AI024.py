#1番取れるところ
import random

class AI28(object):
    def name(self):
        return 'AI2'

    def play(self, board, color):
      X=[]
      Y=[]
      M=[]
      max=0
      min=1000000000
      if board.put_and_reverse(0, 0, color, reverse=False) > 0:
        X.append(0)
        Y.append(0)
      elif board.put_and_reverse(5, 5, color, reverse=False) > 0:
        X.append(5)
        Y.append(5)
      elif board.put_and_reverse(5, 0, color, reverse=False) > 0:
        X.append(5)
        Y.append(0)
      elif board.put_and_reverse(0, 5, color, reverse=False) > 0:
        X.append(0)
        Y.append(5)
      else:
          for y in range(board.N):
            for x in range(board.N):
              if board.put_and_reverse(x, y, color, reverse=False) > 0:
                if max< board.put_and_reverse(x, y, color, reverse=False):
                  max= board.put_and_reverse(x, y, color, reverse=False)
                  X.append(x)
                  Y.append(y)
      return (X[len(X)-1], Y[len(Y)-1])



blackAI = AI28()
whiteAI = RandomAI2()
game(blackAI, whiteAI)
