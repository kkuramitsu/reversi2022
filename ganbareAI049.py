class ganbareAI(object):
      def name(self):
          return 'ganbare049'

      def play(self, board, color):
          while True:
              import random
              x = random.randint(0, board.N+1)
              y = random.randint(0, board.N+1)
              if board.put_and_reverse(x, y, color, reverse=False) > 0:
                  return (x, y)
