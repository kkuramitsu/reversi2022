#
# オセロ（リバーシ）
#
from reversi2022.reversi import *
# from reversi import *
import numpy as np
import random


def find_all(board, color, randomize=False):
    ss = []
    for y in range(board.N):
        for x in range(board.N):
            if board.put_and_reverse(x, y, color, reverse=False) > 0:
                ss.append((x, y))
    if len(ss) > 0 and randomize:
        random.shuffle(ss)
    return ss


default_matrix = np.array([
    [150, 1, 56, 57, 10, 152],
    [1, 0, 10, 10, 0, 10],
    [58, 10, 19, 18, 10, 55],
    [54, 10, 17, 16, 10, 52],
    [10, 0, 10, 10, 0, 10],
    [151, 10, 53, 59, 10, 153],
])


def score(board, color, matrix=default_matrix):
    return (board.b*matrix).sum()*color


def place_a(board, color, matrix=default_matrix):
    lists = find_all(board, color)
    if len(lists) == 0:
        return 0
    ss = []
    s0 = score(board, color)
    for x, y in lists:
        nb = board.copy()
        nb.put_and_reverse(x, y, color)
        s = score(nb, color, matrix)
        ss.append((s-s0, x, y))
    ss.sort()
    s, x, y = ss[-1]
    board.put_and_reverse(x, y, color)
    return s


class MaruAI(object):
    def name(self):
        return 'しほまる'

    MATRIX = np.array([
        [150, 10, 50, 50, 10, 150],
        [10, 0, 10, 10, 0, 10],
        [50, 10, 20, 20, 10, 50],
        [50, 10, 20, 20, 10, 50],
        [10, 0, 10, 10, 0, 10],
        [150, 10, 50, 50, 10, 150],
    ])

    def play(self, board, color):
        ss = []
        s0 = score(board, color, MaruAI.MATRIX)
        for x, y in find_all(board, color, randomize=True):
            nb = board.copy()
            nb.put_and_reverse(x, y, color)
            s = score(nb, color, MaruAI.MATRIX)
            assert s > s0
            ss.append((s-s0, x, y))
        ss.sort()
        _, x, y = ss[-1]
        return x, y


class PanAI(object):
    def name(self):
        return 'ぱん'

    MATRIX = np.array([
        [150, 1, 56, 57, 10, 152],
        [1, 0, 10, 10, 0, 10],
        [58, 10, 19, 18, 10, 55],
        [54, 10, 17, 16, 10, 52],
        [10, 0, 10, 10, 0, 10],
        [151, 10, 53, 59, 10, 153],
    ])

    def play(self, board, color):
        ss = []
        s0 = score(board, color, PanAI.MATRIX)
        for x, y in find_all(board, color):
            nb = board.copy()
            nb.put_and_reverse(x, y, color)
            s = score(nb, color, PanAI.MATRIX)
            assert s > s0
            a = place_a(nb, -color, PanAI.MATRIX)
            if a > 140:
                ax, ay = x, y
                continue
            ss.append((s-s0, x, y))
        ss.sort(reverse=True)
        # print(self.name(), ss)
        if len(ss) == 0:  # どこもおけなかったら四角を取らせる
            return ax, ay
        _, x, y = ss[0]
        return x, y


def deep_score(board, color, matrix, s0, depth=3):
    if depth == 0:
        return score(board, color, matrix) - s0
    ss = []
    for x, y in find_all(board, color):
        nb = board.copy()
        nb.put_and_reverse(x, y, color)
        a = place_a(nb, -color, matrix)
        s = deep_score(nb, color, matrix, s0, depth-1)
        ss.append(s)
    if len(ss) == 0:  # どこもおけない
        return score(board, color, matrix) - s0
    return max(ss) - s0


class TeruAI(object):
    def name(self):
        return 'てるち'

    MATRIX = np.array([
        [150,  -30,  56,  57,  -32,  152],
        [-30,   -70,  20,  20,  -72,  -32],
        [58,   20,   19,   18,   20,   55],
        [54,   20,   17,   16,   20,   52],
        [-31,  -71,  20,  20,  -73,  -33],
        [151,  -31,   53,  59,  -33,  153],
    ])

    def play(self, board, color):
        ss = []
        s0 = score(board, color, TeruAI.MATRIX)
        for x, y in find_all(board, color):
            nb = board.copy()
            nb.put_and_reverse(x, y, color)
            a = place_a(nb, -color, TeruAI.MATRIX)
            # ２手先まで読んで、得点の高いものを探す
            s = deep_score(board, color, TeruAI.MATRIX, s0, 2)
            ss.append((s - a, x, y))
        ss.sort(reverse=True)
        # print(f'\033[31m{self.name()}先読み: {ss}\033[0m')
        _, x, y = ss[0]
        return x, y


if __name__ == '__main__':
    maruAI = MaruAI()
    panAI = PanAI()
    teruAI = TeruAI()
    game10(maruAI, panAI)
    game10(panAI, teruAI)
    game10(teruAI, maruAI)
