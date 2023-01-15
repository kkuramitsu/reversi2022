import random
from reversi2022.reversi import *

class SaraAI(object):
    def name(self):
        return 'sara039'

    def play(self, board, color):
        table = [[5,3,4,4,3,5], [2,1,2,2,1,2], [4,2,0,0,2,4], [4,2,0,0,2,4], [2,1,2,2,1,2], [5,3,4,4,3,5]]
        
        # 現在の局面と色を受け取り、色を置く場所(x,y)を返す
        M = [0, [0, 0]]
        for x in range(0, board.N):
            for y in range(0, board.N):
                if M[0] < board.put_and_reverse(x, y, color, reverse=False)*table[x][y] or (M[0] == board.put_and_reverse(x, y, color, reverse=False)*table[x][y] and random.choice([True,False])):
                    M[0] = board.put_and_reverse(x, y, color, reverse=False)*table[x][y]
                    M[1] = [x, y]
        if M[0] != 0:
            return (M[1][0], M[1][1])
