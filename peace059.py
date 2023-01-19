import numpy as np
class peaceAI(object):
    def name(self):
        return 'peace059'

    def play(self, board, color):
      can_set_pos = []
      can_get_stones = []
      selection = []

      for y in range(board.N):
            for x in range(board.N):
                num = board.put_and_reverse(x, y, color, reverse=False)
                if num > 0:
                    can_set_pos.append((x, y))
                    can_get_stones.append(num)

      for i in range(len(can_set_pos)):
            if can_get_stones[i] == max(can_get_stones):
                selection.append(can_set_pos[i])

      x, y = selection[np.random.randint(0, len(selection))]

      return x, y
