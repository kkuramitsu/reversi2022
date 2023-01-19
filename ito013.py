import random


class OseroAI(object):

  def name(self):
    return 'ito013'

  def play(self, board, color):

    pos_list = []
    gain_list = []
    index_list = []

    for y in range(board.N):
        for x in range(board.N):
            gain = board.put_and_reverse(x, y, color, reverse=False)
            if gain > 0:
                pos_list.append((x, y))
                gain_list.append(gain)

    max_gain = max(gain_list)
    for i, val in enumerate(gain_list):
            if max_gain == val:
                index_list.append(i)
    
    tgt = random.randint(0, len(index_list)-1)


    x, y = pos_list[index_list[tgt]]


    return x, y
  
