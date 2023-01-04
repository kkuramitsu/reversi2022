#評価表を作成し、ポイントが高いところに置く。
#同じポイントの場合、序盤・中盤(空きマス11より多いとき)は相手の石を取る数を最も少ないところに置く(あまりとらない方がいいと聞いたので)。
#終盤(空きマス11以下)は最もたくさん取れるところに置く。

class yui026AI(object):
    def name(self):
        return 'yui026'

    def play(self, board, color):
        import random
        #評価表 四隅=5, 中央壁際=4, 中央=3, 角手前上下=2, 角手前斜め=1
        hyouka = [
        [5, 2, 4, 4, 2, 5],
        [2, 1, 3, 3, 1, 2],
        [4, 3, 0, 0, 3, 4],
        [4, 3, 0, 0, 3, 4],
        [2, 1, 3, 3, 1, 2],
        [5, 2, 4, 4, 2, 5],
        ]
        pos_list = []
        gain_list = []
        point_list = []
        index_list = []
        indexgain_list = []
        index_list2 = []
        a = 0
        while True:
            for i in range(0, board.N):
                for j in range(0, board.N):
                  if board.put_and_reverse(i, j, color, reverse=False) > 0:
                    pos_list.append(6*j+i) #6*j+i何マス目
                    gain_list.append(board.put_and_reverse(i, j, color, reverse=False))
                    point_list.append(hyouka[i][j])
                  if board.b[i][j] == 0:
                    a += 1
            
            max_point = max(point_list)
            for i, val in enumerate(point_list):
              if max_point == val:
                index_list.append(pos_list[i])
                indexgain_list.append(gain_list[i])

            if a > 11:
              min_indexgain = min(indexgain_list)
              for i, val in enumerate(indexgain_list):
                if min_indexgain == val:
                  index_list2.append(index_list[i])

            else:
              max_indexgain = max(indexgain_list)
              for i, val in enumerate(indexgain_list):
                if max_indexgain == val:
                  index_list2.append(index_list[i])

            tgt = random.randint(0, len(index_list2)-1)
            y = index_list2[tgt] // 6
            x = index_list2[tgt] % 6
            return (x, y)
