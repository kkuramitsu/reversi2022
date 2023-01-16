from reversi2022.reversi import *
import  random

class AI(object):
    def name(self):
        return 'mofumofu045'

    def play(self, board, color):
      list = [20,-10,0,0,-10,20
               -10,-5,-2,-2,-5,-10,
                0,-2,0,0,-2,0,
                0,-2,0,0,-2,0,
               -10,-5,-2,-2,-5,-10,
                20,-10,0,0,-10,20]
      while True:
            x=random.randint(0, board.N+1)
            y=random.randint(0, board.N+1)
            if board.put_and_reverse(x,y,color,reverse=False)>0:
                return (x,y) 
