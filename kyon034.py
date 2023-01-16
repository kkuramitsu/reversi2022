from reversi2022.reversi import *
from reversi2022.canvas import game2
import random


def get_key_from_value(d, val):
  keys = [k for k, v in d.items() if v == val]
  if keys:
    return random.choice(keys)
  return [6,6]

# 貪欲法クラス
class GreedAI(GameAI):
  def name(self):
    return '貪欲なAI'
  
  def play(self, board, color):
    l_score = {}
    for y in range(board.N):
      for x in range(board.N):
        s = board.put_and_reverse(x, y, color, reverse=False)
        if  s> 0:
          l_score[(x,y)] = s
    key = get_key_from_value(l_score, max(l_score.values()))
    return (key)

# 評価表クラス
class TableAI(GameAI):
  def name(self):
    return '評価表を使ったAI'

  def play(self, board, color):
    l_score = {}
    score = [[30, -5, 10, 10, -5, 30],[-5, 0, 5, 5, 0, -5], [10, 5, 0, 0, 5, 10], [10, 5, 0, 0, 5, 10], [-5, 0, 5, 5, 0, -5], [30, -5, 10, 10, -5, 30]]
    for y in range(board.N):
      for x in range(board.N):
        if board.put_and_reverse(x, y, color, reverse=False) > 0:
          s = score[x][y]
          l_score[(x,y)] = s
    key = get_key_from_value(l_score, max(l_score.values()))
    return (key)

# 評価表と貪欲のミックス
class Greed_and_TableAI(GameAI):
  def name(self):
    return '034のAI'

  def play(self, board, color):
    corner = [(0,0),(0,5),(5,0),(5,5)]
    l_score = {}
    for y in range(board.N):
      for x in range(board.N):
        s = board.put_and_reverse(x, y, color, reverse=False)
        if  s> 0:
          l_score[(x,y)] = s
    for i in l_score.keys():
      if i in corner:
        return i
    c = np.count_nonzero(board.b==0)
    if c >= 24:
      AI = GreedAI()
      return AI.play(board, color)
    else:
      AI = TableAI()
      return AI.play(board, color)
