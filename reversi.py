#
# オセロ（リバーシ）
#

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

    def show(self):
        counter = Counter()
        for y in range(self.N):
            for x in range(self.N):
                color = self.b[y, x]
                print(stone(color), end='')
                counter.update([stone(color)])
            print()
        print(counter.most_common())
        print()

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


def game(blackAI, whiteAI):
    board = Board()
    board.show()
    while board.can_put(BLACK) or board.can_put(WHITE):
        if board.can_put(BLACK):
            x, y = blackAI.play(board.copy(), BLACK)
            c = board.put_and_reverse(x, y, BLACK)
            if c == 0:
                print(f'{blackAI.name()}は({x},{y})に置こうとした. 反則負け')
                return
            board.show()
        if board.can_put(WHITE):
            x, y = whiteAI.play(board.copy(), WHITE)
            c = board.put_and_reverse(x, y, WHITE)
            if c == 0:
                print(f'{whiteAI.name()}は({x},{y})に置こうとした. 反則負け')
                return
            board.show()


if __name__ == '__main__':
    blackAI = OchibiAI()
    whiteAI = GameAI()
    game(blackAI, whiteAI)
