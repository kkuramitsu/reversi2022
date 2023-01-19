import random

class OnigiriAI(object):
    # 評価表を設定(とりあえず6x6に対応)
    board_eval = [
        [10, -10, -6, -6, -10, 10],
        [-10, -6, -4, -4, -6, -10],
        [-6, -4,  0,  0, -4, -6],
        [-6, -4,  0,  0, -4, -6],
        [-10, -6, -4, -4, -6, -10],
        [10, -10, -6, -6, -10, 10],
    ]

    def name(self):
        return 'おにぎりAI'

    # 自分が石を置ける場所を探索し、おきたい場所の座標を返す
    def play(self, board, color):
        can_set_pos = []
        can_get_stones = []
        pos_evals = []
        selection = []
        final_selection = []

        for y in range(board.N):
            for x in range(board.N):
                num = board.put_and_reverse(x, y, color, reverse=False)
                if num > 0:
                    # 石がとれる位置ととれる石の数をリストに挿入
                    can_set_pos.append((x, y))
                    can_get_stones.append(num)

        # とれる石の数が多いものを選び、それぞれの位置の評価値を加算して候補をさらに絞る。
        # 評価値が同じならば、その中からランダムに決定する。
        for i in range(len(can_set_pos)):
            if can_get_stones[i] == max(can_get_stones):
                bx = can_set_pos[i][0]
                by = can_set_pos[i][1]
                eval = can_get_stones[i] + self.board_eval[bx][by]
                pos_evals.append(eval)
                selection.append(can_set_pos[i])

        for i in range(len(selection)):
            if pos_evals[i] == max(pos_evals):
                final_selection.append(selection[i])
        x, y = final_selection[random.randrange(len(final_selection))]
        return x, y
