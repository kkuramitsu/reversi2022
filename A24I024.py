class A24I(object):
    def name(self):
        return 'A24I'

    def play(self, board, color):
      X=[]
      Y=[]
      M=[]
      max=0
      ok=0
      if board.put_and_reverse(0, 0, color, reverse=False) > 0:
        X.append(0)
        Y.append(0)
      elif board.put_and_reverse(5, 5, color, reverse=False) > 0:
        X.append(5)
        Y.append(5)
      elif board.put_and_reverse(5, 0, color, reverse=False) > 0:
        X.append(5)
        Y.append(0)
      elif board.put_and_reverse(0, 5, color, reverse=False) > 0:
        X.append(0)
        Y.append(5)
      else:
        for y in range(board.N):
          for x in range(board.N):
            if (x==1 and y==1) or (x==1 and y==4) or (x==4 and y==1) or (x==4 and y==4):
              pass
            elif board.put_and_reverse(x, y, color, reverse=False) > 0:
              if max< board.put_and_reverse(x, y, color, reverse=False):
                max= board.put_and_reverse(x, y, color, reverse=False)
                X.append(x)
                Y.append(y)
                ok+=1
        if ok==0:
          M=[1,4]
          N=[1,4]
          for i in range(2):
            for j in range(2):
              if board.put_and_reverse(M[i], N[j], color, reverse=False) > 0:
                if max< board.put_and_reverse(M[i], N[j], color, reverse=False):
                  max= board.put_and_reverse(M[i], N[j], color, reverse=False)
                  X.append(M[i])
                  Y.append(N[j])
      return (X[len(X)-1], Y[len(Y)-1])
