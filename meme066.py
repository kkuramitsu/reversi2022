#提出用
#Min-Max法

import random
class memeAI(object):
    def name(self):
        return'AyariさんのAI'

    def play(self, board, color):
        for y in range(board.N):
            for x in range(board.N):
                if board.put_and_reverse(x, y, color, reverse=False) > 0:
                    return (x, y)

    def computerAi_1stGainMax(self, pos_list, gain_list): 
        index_list = [] 
        max_gain = max(gain_list) 
        for i, val in enumerate(gain_list): 
            if max_gain == val: 
                index_list.append(i) 

        tgt = random.randint(0, len(index_list)-1) 
        return pos_list[index_list[tgt]]

        def computerAi_MinMax_3(self, pos_list, gain_list):
            value = []
            update_pos_list = []

            self.log_on = False 
            value = self.minMax(2, 2, pos_list, gain_list)
            for i, pos in enumerate(pos_list):
                if max(value) == value[i]:
                    update_pos_list.append(pos)

            self.log_on = True
            tgt = random.randint(0, len(update_pos_list)-1)
            return update_pos_list[tgt]

    def minMax(self, depth, max_depth, pos_list, gain_list):  # depth > 0
        value = []
        next_value = []
        next_pos_list = []
        next_gain_list = []
        self.backUpAllState(self.state_storage_list[depth])
        for pos in pos_list:
            ret =  self.putComputerStone(pos, False)
            next_pos_list, next_gain_list = self.scanPuttableCell()
            if (depth > 1):
                next_value = self.minMax(depth-1, max_depth, next_pos_list, next_gain_list)
                if len(next_value) == 0:
                    value.append(0)
                elif (max_depth - depth) % 2 == 0:
                    value.append(min(next_value))
                else:
                    value.append(max(next_value))
            else:
                if len(next_gain_list) == 0:
                    value.append(0)
                elif (max_depth - depth) % 2 == 0:
                    value.append(min(next_gain_list))
                else:
                    value.append(max(next_gain_list))

            self.restoreAllState(self.state_storage_list[depth])

        return value
