from reversi2022.reversi import *
import  random

class mofuAI(object):
    def name(self):
        return 'mofumofu045'

    def play(self, board, color):
      list = [[30,-5,10,10,-5,30],
              [-5,0,5,5,0,-5],
              [10,5,0,0,5,10],
              [10,5,0,0,5,10],
              [-5,0,5,5,0,-5],
              [30,5,10,10,-5,30]]

      w = []
      p = []

      for y in range(board.N):
          for x in range(board.N):
            if board.put_and_reverse(x, y, color, reverse = False) > 0:
              w.append([list[y][x]])
              p.append((x,y))
      a = w.index(max(w))
               
      return p[a]


class AI(object):
    def name(self):
        return 'mofumofu045'
        
def play(self,board, color):	
	a = []

	rank1=[0,5,30,35]
	rank2=[1,4,6,11,24,29,31,34]
	rank3=[2,3,12,17,18,23,32,33]
	rank4=[7,10,25,28]
	rank5=[8,9,13,16,19,22,26,27]
	rank6=[14,15,20,21]

	for position in rank1:
		if put_and_reverse(board, position, color):
			a.append(position)
			if len(a) > 0:
				return random.choice(a)
    
	for position in rank3:
		if put_and_reverse(board, position, color):
			a.append(position)
			if len(a) > 0:
				return random.choice(a)
    
	for position in rank5:
		if put_and_reverse(board, position, color):
			a.append(position)
			if len(a) > 0:
				return random.choice(a)
    
	for position in rank6:
		if put_and_reverse(board, position, color):
			a.append(position)
			if len(a) > 0:
				return random.choice(a)
    
	for position in rank2:
		if put_and_reverse(board, position, color):
			a.append(position)
			if len(a) > 0:
				return random.choice(a)
    
	for position in rank4:
		if put_and_reverse(board, position, color):
			a.append(position)
			if len(a) > 0:
				return random.choice(a)

	return 0
