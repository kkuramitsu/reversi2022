#
# オセロ（リバーシ）
#

import time
from collections import Counter
import numpy as np

BLACK = -1  # 黒
EMPTY = 0  # 空
WHITE = 1  # 白


def reverse(color):
    '''
    色を反転する
    '''
    return -color


STONE = ['●', '□', '○']


def stone(color):
    '''
    色を石文字に変換する
    '''
    return STONE[color+1]


class Board(object):
    N: int
    b: np.ndarray

    def __init__(self, N=6):
        self.N = N
        self.b = np.zeros((N, N), dtype=int)
        c = N//2
        self.b[c, c] = BLACK
        self.b[c, c-1] = WHITE
        self.b[c-1, c] = WHITE
        self.b[c-1, c-1] = BLACK

    def __repr__(self):
        return repr(self.b)

    def show(self, black='', white=''):
        counter = Counter()
        for y in range(self.N):
            for x in range(self.N):
                color = self.b[y, x]
                print(stone(color), end='')
                counter.update([stone(color)])
            print()
        print(counter.most_common())
        print()

    def count(self):
        b = self.b.flatten()
        return abs(b[b == BLACK].sum()), b[b == WHITE].sum()

    def on(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N

    def put_and_reverse(self, x, y, color, reverse=True):
        if not self.on(x, y) or self.b[y, x] != EMPTY:
            return 0

        reversibles = []
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                rs = self.find_reversibles(x, y, dx, dy, color)
                reversibles.extend(rs)

        if reverse and len(reversibles) > 0:
            self.b[y, x] = color
            for xt, yt in reversibles:
                self.b[yt, xt] = color
        return len(reversibles)

    def find_reversibles(self, sx, sy, dx, dy, color):
        rs = []
        for i in range(1, self.N+2):
            x = sx+dx*i
            y = sy+dy*i
            if self.on(x, y):
                if self.b[y, x] == -color:
                    rs.append((x, y))
                    continue
                if self.b[y, x] == color:
                    return rs
            break
        return []

    def can_put(self, color):
        for y in range(self.N):
            for x in range(self.N):
                if self.put_and_reverse(x, y, color, reverse=False) > 0:
                    return True
        return False

    def copy(self):
        d = Board(self.N)
        d.b = self.b.copy()
        return d

# プレイが継続できるか？
# つまり、まだ石を置けるところが残っているか調べる？


class GameAI(object):
    def name(self):
        return self.__class__.__name__

    def play(self, board, color):
        return (6, 6)


class OchibiAI(object):
    def name(self):
        return 'おちびAI'

    def play(self, board, color):
        for y in range(board.N):
            for x in range(board.N):
                if board.put_and_reverse(x, y, color, reverse=False) > 0:
                    return (x, y)


def game(blackAI, whiteAI, verbose=True):
    board = Board()
    if verbose:
        board.show()
    bts, wts = [], []
    while board.can_put(BLACK) or board.can_put(WHITE):
        if board.can_put(BLACK):
            start = time.time()
            x, y = blackAI.play(board.copy(), BLACK)
            bts.append(time.time()-start)
            c = board.put_and_reverse(x, y, BLACK)
            if c == 0:
                print(f'{blackAI.name()}は({x},{y})に置こうとした. 反則負け')
                return 0, 36
            if verbose:
                board.show()
        if board.can_put(WHITE):
            start = time.time()
            x, y = whiteAI.play(board.copy(), WHITE)
            wts.append(time.time()-start)
            c = board.put_and_reverse(x, y, WHITE)
            if c == 0:
                print(f'{whiteAI.name()}は({x},{y})に置こうとした. 反則負け')
                return 36, 0
            if verbose:
                board.show()
    bs, ws = board.count()
    return bs, ws, sum(bts), sum(wts)


def stat(b, w, bs, ws):
    return bs+b, ws+w


def judge(b, w, bwin, bdraw):
    if b > w:
        bwin += 1
    elif b == w:
        bdraw += 0
    return bwin, bdraw


def game10(blackAI, whiteAI=OchibiAI(), N=5):
    bs, ws = 0, 0
    bt, wt = 0, 0
    bwin, bdraw = 0, 0
    for _ in range(N):
        b, w, b2, w2 = game(blackAI, whiteAI, verbose=False)
        bs, ws = stat(b, w, bs, ws)
        bt, wt = stat(b2, w2, bt, wt)
        bwin, bdraw = judge(b, w, bwin, bdraw)
        print(STONE[0], blackAI.name(), b, STONE[2], whiteAI.name(), w)
        b, w, b2, w2 = game(whiteAI, blackAI, verbose=False)
        print(STONE[0], whiteAI.name(), b, STONE[2], blackAI.name(), w)
        bs, ws = stat(w, b, bs, ws)
        bt, wt = stat(w2, b2, bt, wt)
        bwin, bdraw = judge(w, b, bwin, bdraw)
    wwin = N*2-bwin-bdraw
    print(
        f'\033[31m結果\033[0m: {blackAI.name()} {bwin}勝 {whiteAI.name()} {wwin}勝 引き分け {bdraw}')
    print(f'思考時間: {blackAI.name()} {bt:.3f} {whiteAI.name()} {wt:.3f}')
    print(f'得点: {blackAI.name()} {bs} {whiteAI.name()} {ws}')


if __name__ == '__main__':
    blackAI = OchibiAI()
    whiteAI = GameAI()
    game(blackAI, whiteAI)
