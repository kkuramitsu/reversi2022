import numpy as np

class ShionAI(object):
    def name(self):
        return 'ShionAI'

    def play(self, board, color):
        #貪欲AI
        put = [] # おける位置
        get = [] # とれるの数
        O = [] #おける位置の重み
        
        MP = [] #石数最大の位置
        MO = [] #石数最大の時の重み
        can = [] # 最大取れる位置

        #重みづけ
        rank = [[ 5,-1, 4, 4,-1, 5],
                [-1,-2, 1, 1,-2,-1], 
                [ 4, 1, 2, 2, 1, 4], 
                [ 4, 1, 2, 2, 1, 4], 
                [-1,-2, 1, 1,-2,-1], 
                [ 5,-1, 4, 4,-1, 5]]


        #石を置けるすべての位置、取れる数は？？
        for y in range(board.N):
            for x in range(board.N):
                if board.put_and_reverse(x, y, color, reverse=False) > 0: #取れる数が０以上の時
                    put.append((x, y))
                    get.append(board.put_and_reverse(x, y, color, reverse=False))
                    O.append(rank[x][y])#おける位置での重み

        #取れる数が最大
        for i in range(len(put)):
            if get[i] == max(get):
                 MP.append(put[i])#位置
                 MO.append(O[i])#重み

        #取れる数が最大の時に、重み一番大きい
        for i in range(len(MP)):    
            if MO[i] == max(MO):
                can.append(MP[i])
        

        x, y = can[np.random.randint(0, len(can))]
        return x, y
