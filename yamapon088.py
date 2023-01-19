class yamaponAI(object):
  def name(self):
    return 'やまぽんAI'

  def play(self,board,color):
      possible=[]
      weight= [[100, -20, 20, 20, -20, 100],
               [-20, -50, 10, 10, -50, -20],
               [20, 10, 0, 0, 10, 20],
               [20, 10, 0, 0, 10, 20],
               [-20, -50, 10, 10, -50, -20],
               [100, -20, 20, 20, -20, 100]]

      for x in range(board.N):
        for y in range(board.N):
          if board.put_and_reverse(x, y, color, reverse=False) > 0: 
            index=max(weight[x][y])
            possible.append((x,y))

      return possible[index]
