class AI(object):
    def name(self):
        return 'STry053'
        
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.board[3][3] = self.board[4][4] = 1
        self.board[3][4] = self.board[4][3] = -1
        self.turn = 1
 
    def play(self, x, y):
        if not (0 <= x < 8 and 0 <= y < 8):
            return False
        if self.board[x][y] != 0:
            return False
 
        flip_list = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                flip_list += self.search_line(x, y, dx, dy)
 
        if len(flip_list) == 0:
            return False
 
        for (nx, ny) in flip_list:
            self.board[nx][ny] = self.turn
        self.board[x][y] = self.turn
        self.turn = -self.turn
        return True

      
    def search_line(self, x, y, dx, dy):
        flip_list = []
        nx, ny = x + dx, y + dy
        if not (0 <= nx < 8 and 0 <= ny < 8):
            return []
        if self.board[nx][ny] == self.turn:
            return []
        while True:
            nx, ny = nx + dx, ny + dy
            if not (0 <= nx < 8 and 0 <= ny < 8):
                return []
            if self.board[nx][ny] == 0:
                return []
            if self.board[nx][ny] == -self.turn:
                flip_list.append((nx, ny))
            else:
                return flip_list
 
    def alphabeta(state, depth, alpha, beta):
      if depth == 0:
        return evaluate(state)

      if state.turn == 1:
        value = -float('inf')
        for action in get_actions(state):
            value = max(value, alphabeta(do_action(state, action), depth - 1, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
      
      def play(self, board, color):
        while True:
            s = value
            t = alpha
            if board.put_and_reverse(s, t, color, reverse=False) > 0:
                return (s, t)

 
