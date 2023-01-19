from reversi2022.reversi import *


class mytAI(object):
    def name(self):
        return 'myt083'

    def play(self, board, color):
      point = []
      index = []
      eval_board = [  # どのマスに石があったら何点かを表す評価ボード
      [ 30, -12,  0,  0, -12,  30],
      [-12, -15, -3, -3, -15, -12],
      [  0,  -3,  -1,  -1,  -3,   0],
      [  0,  -3,  -1,  -1,  -3,   0],
      [-12, -15, -3, -3, -15, -12],
      [ 30, -12,  0,  0, -12,  30]
      ]

      for x in range(board.N):
        for y in range(board.N):
          if board.put_and_reverse(x, y, color, reverse=False) > 0: # 0以上だったら置ける
            point.append(eval_board[x][y])
            index.append([x,y])
      ans = point.index(max(point))
      return index[ans]  
