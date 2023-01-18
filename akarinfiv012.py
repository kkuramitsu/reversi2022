##必要モジュール
from reversi2022.reversi import *
import random
from collections import Counter
import numpy as np
import sys

class akarinfivAI(GameAI):
    def name(self):
        return 'akarinfiv012'

    def play(self, board, color):

        ##貪欲AIを作ってみる。
        #まずは重みづけ
        rank = [
        [-11, -16, -1, -1, -16, -11],
        [  4,  -1,  2,  2,  -1,   4],
        [ -1,  -3, -1, -1,  -3,  -1],
        [ -1,  -3, -1, -1,  -3,  -1],
        [  4,  -1,  2,  2,  -1,   4],
        [-11, -16, -1, -1, -16, -11],
        ]

        dir=0

        if board[position] != EMPTY:
            return dir

        put_list = [] #置く位置
        get_list = [] #もらえる
        point_list = [] #おもみ
        max_list = []
        maxget_list = []
        max_list2 = []

#黒い石、白い石がある数を確認
        b=0
        w=0
        for y in range(6):
            for x in range(6):
                 if board[y][x]==BLACK:
                     b+=1
                 if board[y][x]==WHITE:
                     w+=1
                     return b,w

        while True:
          x = random.randint(0, board.N+1)
          y = random.randint(0, board.N+1)

        for y in range(board.N):
            for x in range(board.N):
                if board.put_and_reverse(x, y, color, reverse=False)>0:
                    put_list.append((x, y))
                    get_list.append(board.put_and_reverse(x, y, color, reverse=False))
                    point_list.append(rank[x][y])

        for i in range(len(put_list)):
            if get_list[i] == max(get_list):
                 max_list.append(put_list[i])
                 maxget_list.append(point_list[i])

        for i in range(len(max_list)):    
            if maxget_list[i] == max(maxget_list):
                max_list2.append(max_list[i])

#そこに置くと返せる数を確認
        if (rank[y][x])>0:
            return -1
        total=0

        for dy in range(-1,2):
           for dx in range(-1,2):
                k=0
                sx=x
                sy=y
                while True:
                   sx+=dx
                   sy+=dy
                   if sx<0 or sx>5 or sy<0 or sy>5:
                     break
                     if board[sy][sx]==0:
                        break
                     if board[sy][sx]==3-color:
                        k+=1
                     if board[sy][sx]==color:
                        total+=k
                        break
                        return total

#置けるか確認

        for y in range(6):
          for x in range(6):
            if returns(x,y,color)>0:
              return True
            return False



        x, y = max_list2[np.random.randint(0, len(max_list2))]
        return x, y
