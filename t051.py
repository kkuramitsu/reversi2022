from reversi2022.reversi import *
import random

class O51AI(object):
    def name(self):
        return 'AI'

    def play(self, board, color):
        point = [[6,2,5,4,4,5,2,6],
                 [2,1,3,3,3,3,1,2],
                 [5,3,3,3,3,3,3,5],
                 [4,3,3,0,0,3,3,4],
                 [4,3,3,0,0,3,3,4],
                 [5,3,3,3,3,3,3,5],
                 [2,1,3,3,3,3,1,2],
                 [6,2,5,4,4,5,2,6]]
        sx = 0
        sy = 0
        p = 0
        for y in range(board.N):
            for x in range(board.N):
                if board.can_put(color):
                    if point[y][x] > p:
                        p = point[y][x]
                        sx = x
                        sy = y
        x=sx
        y=sy
        for y in range(board.N):
            for x in range(board.N):
                if board.put_and_reverse(x, y, color, reverse=False) > 0:
                    return(x, y)
