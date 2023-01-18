from reversi2022.reversi import *
import random

class rAI(object):
    def name(self):
        return 'ryoko'

    def play(self, board, color):
        point = [[120,-20,20,5,5,20,-20,120],
        [-20,-40,-5,-5,-5,-5,-40,-20],
        [20,-5,15,3,3,15,-5,20],
        [5,-5,3,3,3,3,-5,5],
        [5,-5,3,3,3,3,-5,5],
        [20,-5,15,3,3,15,-5,20],
        [-20,-40,-5,-5,-5,-5,-40,-20],
        [120,-20,20,5,5,20,-20,120]]
        stone_score = []
        stone_location = []
        for y in range(board.N):
          for x in range(board.N):
            if board.put_and_reverse(x, y, color, reverse=False) > 0:
              stone_score.append(point[y][x])
              stone_location.append((x, y))
        return stone_location[stone_score.index(max(stone_score))]
