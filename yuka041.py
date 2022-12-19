from .reversi import *

class AI(object):
    def name(self):
        return 'yuka041'

    def play(self, board, color):
        score = [[100, -10, 10, 10, -10, 100],
              [-10, -50, -5, -5, -50, -10],
              [10, -5, 0, 0, -5, 10],
              [10, -5, 0, 0, -5, 10],
              [-10, -50, -5, -5, -50, -10],
              [100, -10, 10, 10, -10, 100]]
        value = []
        place = []
        for y in range(board.N):
          for x in range(board.N):
            if board.put_and_reverse(x, y, color, reverse=False) > 0:
              value.append(score[y][x])
              place.append((x, y))
        valueAnswer = max(value)
        placeAnswer = value.index(valueAnswer)
        return place[placeAnswer]
