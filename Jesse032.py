import numpy as np

class OnigiriAI(object):
    def name(self):
        return 'Jesse032'

    def play(self, board, color):
        # それぞれの値を格納するリストを用意
        can_set_pos = [] # 石が置ける位置
        can_get_stones = [] # とれる石の数
        selection = [] # AIがとりうる石の位置


        # オセロ板のすべての位置においてAIが石を置ける位置と、とれる石の個数を調べる
        for y in range(board.N):
            for x in range(board.N):
                num = board.put_and_reverse(x, y, color, reverse=False) # 位置(x, y)でとれる石の数
                if num > 0:
                    # とれる石の数が0個以上ということは、そこに石が置けるということ。
                    # その位置(x, y)ととれる石の数をそれぞれリストに入れる
                    can_set_pos.append((x, y))
                    can_get_stones.append(num)

        
        # とれる石の数が多いものを選ぶ
        # 該当箇所が複数あった場合、その中からランダムで選ぶ
        for i in range(len(can_set_pos)):
            if can_get_stones[i] == max(can_get_stones):
                selection.append(can_set_pos[i])
        
        # AIが選んだ石を置く位置を代入
        x, y = selection[np.random.randint(0, len(selection))]

        return x, y
