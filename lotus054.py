from reversi2022.reversi import *
import random

class lotusAI(GameAI):
    def name(self):
        return 'lotusAI'

    def play(self, board, color):
        hyouka1=[ [100,2,10,10,2,100],
                     [2,1,5,5,1,2],
                     [10,5,0,0,5,10],
                     [10,5,0,0,5,10],
                     [2,1,5,5,1,2],
                     [100,2,10,10,2,100] ]
        
        ooilist = [0, 0, 0, 0]
        for y in range(board.N):
            for x in range(board.N):
                ooi = board.put_and_reverse(x, y, color, reverse=False)
                if ooi > ooilist[0]:
                    hyo = hyouka1[x][y]
                    if hyo > ooilist[1]:
                        ooilist = [ooi, hyo, x, y]

        x = ooilist[-2]
        y = ooilist[-1]
        return (x, y)
