class Paru(object):
  def name(self):
    return 'Paru'

  def play(self, board, color):
      while True:
        A=[]
        for m in range(16):
          if m < 9:
            for i in range(0, board.N+1):
              for j in range(0, board.N+1):
                if board.put_and_reverse(i, j, color, reverse=False) > 0:
                  A.append([board.put_and_reverse(i, j, color), i, j])
                  A.sort()
                  n = len(A)//2
                  return (A[n][1],A[n][2])
                  m += 1
          else:
            for i in range(0, board.N+1):
              for j in range(0, board.N+1):
                if board.put_and_reverse(i, j, color, reverse=False) > 0:
                  A.append([board.put_and_reverse(i, j, color), i, j])
                  A.sort()
                  return (A[0][1], A[0][2])
                  m += 1
