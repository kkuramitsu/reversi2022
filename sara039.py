from reversi2022.reversi import *
import random

class SaraAI(object):
    def name(self):
        return 'sara039'

    def play(self, board, color):
        table = [[50,2,5,5,2,50], [2,1,3,3,1,2], [5,3,0,0,3,5], [5,3,0,0,3,5], [2,1,3,3,1,2], [50,2,5,5,2,50]]
        
        # 現在の局面と色を受け取り、色を置く場所(x,y)を返す
        M = [0, (0, 0)]
        for x in range(0, board.N):
            for y in range(0, board.N):
                if M[0] < board.put_and_reverse(x, y, color, reverse=False)*table[x][y] or (M[0] == board.put_and_reverse(x, y, color, reverse=False)*table[x][y] and random.choice([True,False])):
                    M[0] = board.put_and_reverse(x, y, color, reverse=False)*table[x][y]
                    M[1] = (x, y)
        if M[0] != 0:
            return (M[1])
