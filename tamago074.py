from reversi2022.reversi import *

class tamagoAI(object):
    def name(self):
        return 'tamago'

    def play(self, board, color):
        
        PointList = [[100, -40, 20 ,20, -40, 100],
                     [-40, -80, -1, -1, -80, -40],
                     [20, -1, 5, 5, -1, 20],
                     [20, -1, 5, 5, -1, 20],
                     [-40, -80, -1, -1, -80, -40],
                     [100, -40, 20 ,20, -40, 100]]
        
        NewPointList = []

        for y in range(board.N):
          for x in range(board.N):
            if board.put_and_reverse(x, y, color, reverse=False) > 0: #置けるとき
              NewPointList.append(PointList[x][y])
            else:  #置けないとき
              NewPointList.append(0)

        NewPointArray = []

        for i in range(0, len(NewPointList), board.N):
          NewPointArray.append(NewPointList[i: i+board.N])
        NewPointArray = np.array(NewPointArray)

        MaxCoordinate = np.unravel_index(NewPointArray.argmax(), NewPointArray.shape)
        x = MaxCoordinate[0]
        y = MaxCoordinate[1]

        return (x,y)
