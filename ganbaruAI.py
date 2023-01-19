BOARD = 8 

BLANK = 0  
BLACK = 1  
WHITE = 2  
STONE = ['×', '●', '○']  


def xy(p):    
  return p % N, p // N


def p(x, y):    
  return x + y * N

def init_board():
  board = [BLANK] * (N*N)
  c = N//2
  board[p(c, c)] = BLACK
  board[p(c-1, c-1)] = BLACK
  board[p(c, c-1)] = WHITE
  board[p(c-1, c)] = WHITE
  return board

def show_board(board):
  counts = [0, 0, 0]
  for y in range(N):
    for x in range(N):
      stone = board[p(x, y)]
      counts[stone] += 1
      print(STONE[stone], end='')
    print()
  print()
  for pair in zip(STONE, counts):
    print(pair, end=' ')
  print()



def on_borad(x, y):
  return 0 <= x < N and 0 <= y < N


def try_reverse(board, x, y, dx, dy, color):
  if not on_borad(x, y) or board[p(x, y)] == BLANK:
    return False
  if board[p(x, y)] == color:
    return True
  if try_reverse(board, x+dx, y+dy, dx, dy, color):
    board[p(x, y)] = color
    return True
  return False

def opposite(color):
  if color == BLACK:
    return WHITE
  return BLACK


def is_oposite(board, x, y, color):
  return on_borad(x, y) and board[p(x, y)] == opposite(color)


DIR = [
    (-1, -1), (+0, -1), (+1, -1),
    (-1, +0),           (+1, +0),
    (-1, +1), (+0, +1), (+1, +1)
]



def put_and_reverse(board, position, color): 
  if board[position] != BLANK:
  	return False
  board[position] = color

  x, y = xy(position)
  turned = False
  for dx, dy in DIR:
    nx = x + dx
    ny = y + dy
    if is_oposite(board, nx, ny, color):
      if try_reverse(board, nx, ny, dx, dy, color):
        turned = True
  if not turned:
    board[position] = BLANK
  return turned

def can_play(board, color):
  board = board[:] 
  for position in range(0, N*N):
    if put_and_reverse(board, position, color):
      return True
  return False


def game(player1, player2):
	board = init_board()
	show_board(board)
	oserogame = True  
	while oserogame:
		oserogame = False  
		if can_play(board, BLACK):
			position = player1(board[:], BLACK)
			show_board(board)
			oserogame = put_and_reverse(board, position, BLACK)
		if can_play(board, WHITE):
			position = player2(board[:], WHITE)
			show_board(board)
			oserogame = put_and_reverse(board, position, WHITE)
	show_board(board)  


def ganbaruAI(board, color):
  a = [0,5,30,35,2,3,12,17,18,23,32,33,8,9,13,16,19,22,26,27,1,4,6,11,24,29,31,34,7,10,25,28]
  for i in range(len(a)):
    position =a[i]
    if put_and_reverse(board, position, color):
      return position
  return 0
