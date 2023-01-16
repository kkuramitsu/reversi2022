# 定数
SIZE = 14           # 盤面の大きさ
FIRST_KALAH = 6     # 先手、先手のカラハの位置
SECOND_KALAH = 13   # 後手、後手のカラハの位置
STONE = 72          # 石の個数
EVEN = STONE // 2

NORMAL = 0          # 通常の穴に入った場合
KALAH = 1           # KALAH に入った場合
GAMEOVER = 2        # ゲーム終了

# 盤面
class Board:
    def __init__(self, b):
        self.board = b[:]

    def __getitem__(self, x):
        return self.board[x]

    def copy(self):
        return Board(self.board)
    
        def distribute(self, turn, pos):
        num = self.board[pos]
        self.board[pos] = 0
        while num > 0:
            pos += 1
            if pos == SIZE: pos = 0
            if (turn == FIRST_KALAH and pos == SECOND_KALAH) or \
               (turn == SECOND_KALAH and pos == FIRST_KALAH): continue
            self.board[pos] += 1
            num -= 1
        return pos
    
       def check_capture(self, turn, pos):
        if (turn == FIRST_KALAH and 0 <= pos <= 5) or \
           (turn == SECOND_KALAH and 7 <= pos <= 12):
            if self.board[pos] == 1 and self.board[12 - pos] > 0:
                # 両取りができる
                num = self.board[12 - pos] + 1
                self.board[turn] += num
                self.board[pos] = 0
                self.board[12 - pos] = 0
                return True
        return False
    
        # 穴にある石を数える
    def count_stone(self, turn):
        n = 0
        for x in range(turn - 6, turn): n += self.board[x]
        return n

    # 石をカラハに入れる
    def put_stone_into_kalah(self, turn):
        n = 0
        for x in range(turn - 6, turn):
            n += self.board[x]
            self.board[x] = 0
        self.board[turn] += n
    
    # 終了チェック
    def check_gameover(self):
        if self.count_stone(FIRST_KALAH) == 0:
            self.put_stone_into_kalah(SECOND_KALAH)
            return True
        elif self.count_stone(SECOND_KALAH) == 0:
            self.put_stone_into_kalah(FIRST_KALAH)
            return True
        elif self.board[FIRST_KALAH] > EVEN or \
             self.board[SECOND_KALAH] > EVEN:
            return True
        return False
    
        def move_stone(self, turn, pos):
        pos = self.distribute(turn, pos)
        if pos == turn: return KALAH
        self.check_capture(turn, pos)
        return NORMAL
    
    # 定数
MAX_VALUE = 100     # 評価値の最大値
MIN_VALUE = -100    # 評価値の最小値

# 先手の指し手を選ぶ
def move_first(depth, board):
    if board.check_gameover() or depth == 0:
        # 盤面の評価
        return board.value_func(), []
    #
    value = MIN_VALUE
    move = []
    for pos in range(0, 6):
        if board[pos] == 0: continue
        b = board.copy()
        # 石を動かす
        result = b.move_stone(FIRST_KALAH, pos)
        m = []
        if result == KALAH:
            # 手番は同じまま
            v, m = move_first(depth, b)
        else:
            # 後手番
            v, _ = move_second(depth - 1, b)
        # ミニマックス法 : 先手は大きな値を選ぶ
        if value < v:
            value = v
            move = [pos] + m
    return value, move

def move_second(depth, board):
    if board.check_gameover() or depth == 0:
        # 盤面の評価
        return board.value_func(), []
    #
    value = MAX_VALUE
    move = []
    for pos in range(7, 13):
        if board[pos] == 0: continue
        b = board.copy()
        # 石を動かす
        result = b.move_stone(SECOND_KALAH, pos)
        m = []
        if result == KALAH:
            # 手番は同じまま
            v, m = move_second(depth, b)
        else:
            # 先手番
            v, _ = move_first(depth - 1, b)
        # ミニマックス法 : 後手は小さな値を選ぶ
        if value > v:
            value = v
            move = [pos] + m
    return value, move

def play(first_depth, second_depth, think1 = move_first, think2 = move_second):
    init_count()
    board = Board([6,6,6,6,6,6,0,6,6,6,6,6,6,0])    # 初期状態
    turn = FIRST_KALAH
    while True:
        if turn == FIRST_KALAH:
            value, move = think1(first_depth, board)
        else:
            value, move = think2(second_depth, board)
        # 表示
        for x in move:
            print('move', x)
            board.move_stone(turn, x)
            board.print_board()
            print()
        if board.check_gameover():
            print('Game Over')
            board.print_board()
            print_count()
            return
        if turn == FIRST_KALAH:
            turn = SECOND_KALAH
        else:
            turn = FIRST_KALAH
