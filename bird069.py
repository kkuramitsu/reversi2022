from reversi2022.reversi import *

class birdAI(object):
    def name(self):
        return 'bird069'

    def play(self, board, color):
      board_num = [[ 10,-10, -6, -6,-10, 10],
             [-10, -6, -4, -4, -6,-10],
             [ -6, -4,  0,  0, -4, -6],
             [ -6, -4,  0,  0, -4, -6],
             [-10, -6, -4, -4, -6,-10],
             [ 10,-10, -6, -6,-10, 10]]
      s = []
      t = []

      for i in range(board.N):
        for j in range(board.N):
          if board.put_and_reverse(i, j, color, reverse=False) > 0: 
            s.append(board_num[i][j])
            t.append([i,j])
      ans = s.index(max(s))
      return t[ans]  
