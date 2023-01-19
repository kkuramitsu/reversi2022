from reversi2022.reversi import *
import random

class mmkAI(GameAI):
    def name(self):
        return 'mmkAI'

    def play(self, board, color):
        while True:
            x = random.randint(0, board.N+1)
            y = random.randint(0, board.N+1)
            for y in range(board.N):
              for x in range(board.N):
                if board.put_and_reverse(x, y, color, reverse=False) > 0:
                    return (x, y)

