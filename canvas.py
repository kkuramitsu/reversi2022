import os
from .reversi import *

try:
  import kogi
  from kogi.canvas import Canvas
except:
  os.system('pip install -q kogi')
  import kogi
  from kogi.canvas import Canvas

import math

def draw_stone(ctx, x, y, color, D):
    R = D//2
    ctx.beginPath()
    ctx.arc(x*D+R, y*D+R, R, 0, 2 * math.pi)
    if color == 1:
        ctx.fillStyle = "white"
    else:
        ctx.fillStyle = "black"
    ctx.fill()


def draw_board(canvas, board):
    ctx = canvas.getContext("2d")
    WIDTH=400 # 横
    HEIGHT=300 # 高さ
    D = min(WIDTH//board.N, HEIGHT//board.N) #1マスの大きさ
    R = D//2
    black=0
    white=0
    for x in range(0, board.N):
        for y in range(0, board.N):
            if (x+y) % 2 == 0:
                ctx.fillStyle = "#005438"
            else:
                ctx.fillStyle = "green"
            ctx.fillRect(x*D, y*D, D, D)
            if board.b[y,x] != 0:
                draw_stone(ctx, x, y, board.b[y,x], D)
                if board.b[y,x] == 1:
                    white+=1
                else:
                    black+=1
    ctx.fillStyle='black'
    ctx.font = '48px serif'
    ctx.fillText(f'黒', 6*D+10, 50)
    ctx.fillText(f'{black}', 6*D+10, 100)
    ctx.fillText(f'白', 6*D+10, 150)
    ctx.fillText(f'{white}', 6*D+10, 200)

def game2(blackAI, whiteAI, fps=10):
    canvas = Canvas(fps=fps)
    board = Board()
    print(f'黒 {blackAI.name()} 白 {whiteAI.name()}')
    draw_board(canvas, board)
    while board.can_put(BLACK) or board.can_put(WHITE):
        if board.can_put(BLACK):
            x, y = blackAI.play(board.copy(), BLACK)
            c = board.put_and_reverse(x, y, BLACK)
            if c == 0:
                print(f'{blackAI.name()}は({x},{y})に置こうとした. 反則負け')
                return
            draw_board(canvas, board)
        if board.can_put(WHITE):
            x, y = whiteAI.play(board.copy(), WHITE)
            c = board.put_and_reverse(x, y, WHITE)
            if c == 0:
                print(f'{whiteAI.name()}は({x},{y})に置こうとした. 反則負け')
                return
            draw_board(canvas, board)
    display(canvas)
