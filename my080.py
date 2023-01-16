#評価表＋貪欲
class MyAI(object):
    def name(self):
        return 'myAI'

    def play(self, board, color):
        stones = [] 
        value = []
        place = []
        ans = []
        S = [[5, -4, 3, 3, -4,  5],
            [-4, -5, 1, 1, -5, -4],
            [ 3,  1, 0, 0,  1,  3],
            [ 3,  1, 0, 0,  1,  3],
            [-4, -5, 1, 1, -5, -4],
            [ 5, -4, 3, 3, -4,  5]]
        for y in range(board.N):
          for x in range(board.N):
            if board.put_and_reverse(x, y, color, reverse=False) > 0:
              value.append(S[y][x])
              stones.append(board.put_and_reverse(x, y, color, reverse=False))
              place.append((x, y))
        for i in range(len(value)):
          ans.append(value[i] + stones[i])
        ansmax = max(ans)
        finalAnswer = ans.index(ansmax)
        return place[finalAnswer]
