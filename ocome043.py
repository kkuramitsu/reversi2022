class ocomeAI(object):
  def name(self):
    return 'ocome043'
  
  def play(self, board, color):
    posi = []
    qua = []

    for y in range(board.N):
      for x in range(board.N):
        quantity = board.put_and_reverse(x,y,color,reverse=False) 
        
        if quantity > 0:
          posi.append((x,y))
          qua.append(quantity)
    q_max = max(qua)
    q_index = qua.index(q_max)
    return (posi[q_index])
