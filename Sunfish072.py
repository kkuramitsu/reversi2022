from reversi2022.reversi import *
import random

class AI(object):
    def name(self):
        return 'HM072'
        
    def play(self, board, color):
        weight= [[100, -10, 20, 20, -10, 100],
                 [-10, -50, 1, 1, -50, -10],
                 [20, 1, 1, 1, 1, 20],
                 [20, 1, 1, 1, 1, 20],
                 [-10, -50, 1, 1, -50, -10],
                 [100, -10, 20, 20, -10, 100]]

        row = -1
        col = -1
        wmax = -1
        #全てのマスについて
        for y in range(board.N):
            for x in range(board.N):
                #置けるなら
                if board.can_put(color):
                    #これまでより重みが大きければ
                    if weight[y][x] > wmax:
                        #その場所を記憶
                        wmax = weight[y][x];
                        row = y
                        col = x
        y=row
        x=col
        for y in range(board.N):
            for x in range(board.N):
                if board.put_and_reverse(x, y, color, reverse=False) > 0:
                    return (x, y)  
