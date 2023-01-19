class YunaAI(object):
    def name(self):
        return 'y002'

    def play(self, board, color):
        import random
        hyouka = [
        [10, 4, 8, 8, 4, 10],
        [4, 2, 6, 6, 2, 4],
        [8, 6, 0, 0, 6, 8],
        [8, 6, 0, 0, 6, 8],
        [4, 2, 6, 6, 2, 4],
        [10, 4, 8, 8, 4, 10],
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
                    pos_list.append(6*j+i) 
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
