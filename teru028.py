#
# オセロ（リバーシ）
#
from reversi2022.reversi import *
import numpy as np


def find_all(board, color):
    ss = []
    for y in range(board.N):
        for x in range(board.N):
            if board.put_and_reverse(x, y, color, reverse=False) > 0:
                ss.append((x, y))
    return ss


eval_matrix = np.array([
    [120, 10, 20, 20, 10, 120],
    [10, 5, 10, 10, 5, 10],
    [20, 10, 30, 30, 10, 20],
    [20, 10, 30, 30, 10, 20],
    [10, 5, 10, 10, 5, 10],
    [120, 10, 20, 20, 10, 120],
])


def score(board, color):
    return (board.b * eval_matrix * color).sum()


def place_a(board, color):
    lists = find_all(board, color)
    if len(lists) == 0:
        return
    ss = []
    for x, y in lists:
        nb = board.copy()
        nb.put_and_reverse(x, y, color)
        s = score(nb, color)
        ss.append((s, x, y))
    ss.sort()
    _, x, y = ss[0]
    board.put_and_reverse(x, y, color)


def deep_score(board, color, depth=3):
    if depth == 0:
        return score(board, color)
    ss = []
    for x, y in find_all(board, color):
        nb = board.copy()
        nb.put_and_reverse(x, y, color)
        place_a(nb, -color)
        s = deep_score(board, color, depth-1)
        ss.append(s)
    return max(ss)


class TeruAI(object):
    def name(self):
        return 'てるぱん'

    def play(self, board, color):
        ss = []
        for x, y in find_all(board, color):
            nb = board.copy()
            nb.put_and_reverse(x, y, color)
            place_a(nb, -color)
            s = deep_score(board, color, 3)
            ss.append((s, x, y))
        ss.sort()
        print('先読み', ss)
        _, x, y = ss[-1]
        return x, y


if __name__ == '__main__':
    blackAI = Greed_and_TableAI()
    whiteAI = TeruAI()
    game(blackAI, whiteAI)
