from reversi2022.reversi import *

class ymAI(GameAI):
    def name(self):
      return 'ym089'

    def play(self, board, color):
        list=[[30,-12,0,-1,-1,0,-12,30],
              [-12,-15,-3,-3,-3,-3,-15,-12],
              [0,-3,0,-1,-1,0,-3,0],
              [-1,-3,-1,-1,-1,-1,-3,-1],
              [-1,-3,-1,-1,-1,-1,-3,-1],
              [0,-3,0,-1,-1,0,-3,0],
              [-12,-15,-3,-3,-3,-3,-15,-12],
              [30,-12,0,-1,-1,0,-12,30]]
        s=[]
        t=[]

        for y in range(board.N):
          for x in range(board.N):
            if board.put_and_reverse(x, y, color, reverse=False) > 0:
              s.append(list[x][y])
              t.append((x, y))
        ss = max(s)
        tt = s.index(ss)
        return t[tt]
