from reversi2022.reversi import *
import random

class AI(object):
    def name(self):
        return 'ose075'
        
    def play(self, board, color):
        #評価表
        tablesc= [[150, -10, 20, 20, -10, 150],
                 [-10, -40, 3, 3, -40, -10],
                 [20, 3, 3, 3, 3, 50],
                 [20, 3, 3, 3, 3, 50],
                 [-10, -40, 3, 3, -40, -10],
                 [150, -10, 20, 20, -10, 150]]        
        v=[] #重み
        p=[] #おける場所

        for y in range(board.N):
          for x in range(board.N):
            if board.put_and_reverse(x, y, color, reverse=False) > 0:
              v.append(tablesc[y][x])
              p.append((x,y))

        ans = v.index(max(v))
        return p[ans]
