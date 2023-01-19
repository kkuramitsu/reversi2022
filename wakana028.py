from reversi2022.reversi import *
import random

class wakana028AI(GameAI):
    def name(self):
        return 'wakana028'

    def play(self, board, color):

      put_list = [] #置く位置
      get_list = [] #取得数
      point_list = [] #重み
      max_list = []
      maxget_list = []
      max_list2 = []


      point = [
          [6,2,5,4,4,5,2,6],
          [2,1,3,3,3,3,1,2],
          [5,3,3,3,3,3,3,5],
          [4,3,3,0,0,3,3,4],
          [4,3,3,0,0,3,3,4],
          [5,3,3,3,3,3,3,5],
          [2,1,3,3,3,3,1,2],
          [6,2,5,4,4,5,2,6]
      ]

      for y in range(board.N):
          for x in range(board.N):
              if board.put_and_reverse(x, y, color, reverse=False) > 0: 
                  put_list.append((x, y))
                  get_list.append(board.put_and_reverse(x, y, color, reverse=False))
                  point_list.append(rank[x][y])


      #最大数
      for i in range(len(put_list)):
          if get_list[i] == max(get_list):
                max_list.append(put_list[i])#位置
                maxget_list.append(O[i])#重み

        #最大数の時に、最重量
      for i in range(len(max_list)):
          if maxget_list[i] == max(maxget_list):
                max_list2.append(max_list[i])
        

      x, y = max_list2[np.random.randint(0, len(max_list2))]
      return x, y
