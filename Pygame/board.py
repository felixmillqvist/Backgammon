import numpy as np
import player
B = -1
W = 1
BAR_black = 0
BAR_white = 25
BAR = 0
class Board:
    def __init__(self, white_player, black_player):
        self.board = np.zeros(25, dtype=int)
    
        self.board[1] = -2
        self.board[6] = 5
        self.board[8] = 3
        self.board[12] = -5
        self.board[13] = 5
        self.board[17] = -3
        self.board[19] = -5
        self.board[24] = 2

        self.white = white_player
        self.black = black_player
        
    
    def update(self):
        self.black.home = sum(self.board[19:25][self.board[19:25]<0])
        self.white.home = sum(self.board[1:7][self.board[1:7]>0])
        
        
    def move(self,start_point, die, player):
        
        if player == self.white:
            end_point = start_point - die
            if start_point == BAR:
                if self.board[end_point] == -1:
                    self.board[end_point] += 1
                    self.black.increase_bar()
                    
                self.board[25-die] += 1
                self.white.decrease_bar()
                
            elif end_point < 1:
                if self.white.bearing_off_possible():
                    self.board[start_point] += -1
                    self.white.increase_free()
                
            else:
                if self.board[end_point] == -1:
                    self.board[end_point] += 1
                    self.black.increase_bar()
                self.board[start_point] += -1
                self.board[end_point] += 1
                
        elif player == self.black:
            end_point = start_point + die
            if start_point == BAR:
                if self.board[end_point] == 1:
                    self.board[end_point] += -1
                    self.white.increase_bar()
                self.board[0+die] += -1
                self.black.decrease_bar()
                
            elif end_point > 24:
                if self.black.bearing_off_possible:
                    self.board[start_point] += 1
                    self.black.increase_free() 
                
            else:
                if self.board[end_point] == 1:
                    self.board[end_point] += -1
                    self.white.increase_bar()
                self.board[start_point] += +1
                self.board[end_point] += -1
        
    
    def print(self):
#       W = o
#       B = x
        print('__________________________________________________________', end = '')
        print('__________________________________________________________________')
        print('____WHITE = x_____________________________________________', end = '')
        print('________________________________________o HOME BOARD______________')
        print('| |\t12\t11\t10\t9\t8\t7\t| |\t6\t5\t4\t3\t2\t1\t| | o-FREE:')
        
        for j in range(1,max(abs(self.board))+1): 
            print('| |',end = '')
            for i in range(12,6,-1):
                if self.board[i] >= j:
                    print('\to', end = '')
                elif self.board[i] <= -j:
                    print('\tx', end = '')
                else:
                    print(' \t', end = '')
            print('\t| |', end='')

            for i in range(6,0,-1):
                if self.board[i] >= j:
                    print('\to', end = '')
                elif self.board[i] <= -j:
                    print('\tx', end = '')
                else:
                    print(' \t', end = '')
    
            
            if j != 1 and j != max(abs(self.board))-1 and j != max(abs(self.board)):
                print('\t| |')
            
            if j == 1:
                print('\t| |', end = '')
                print('\t', self.white.free)
                
            if j == max(abs(self.board))-1:
                print('\t| |', end = '')
                print('  o-BAR:')
                
            if j == max(abs(self.board)):
                print('\t| |', end = '')
                print('\t', self.white.bar)
    
        print('| |',end = '')
        print('                                                     ', end = '')
        print('| |',end = '')
        print('                                                     ', end = '')
        print('| |')
        print('----------------------------------------------------------', end = '')
        print('---------------------------------------------------------')
        print('| |',end = '')
        print('                                                     ', end = '')
        print('| |',end = '')
        print('                                                     ', end = '')
        print('| |')
        
        for j in range(max(abs(self.board)),0,-1): 
            print('| |',end = '')
            for i in range(13,19):
                if self.board[i] >= j:
                    print('\to', end = '')
                elif self.board[i] <= -j:
                    print('\tx', end = '')
                else:
                    print(' \t', end = '')
            print('\t| |', end='')
            for i in range(19,25):
                if self.board[i] >= j:
                    print('\to', end = '')
                elif self.board[i] <= -j:
                    print('\tx', end = '')
                else:
                    print(' \t', end = '')
            
            if j != 1 and j != max(abs(self.board))-1 and j != max(abs(self.board)):
                print('\t| |')
            
            if j == 1:
                print('\t| |', end = '')
                print(' x-FREE:')
                
            if j == max(abs(self.board))-1:
                print('\t| |', end = '')
                print('\t', self.black.bar)
                
            if j == max(abs(self.board)):
                print('\t| |', end = '')
                print('  x-BAR:')
            
        print('| |\t13\t14\t15\t16\t17\t18\t| |\t19\t20\t21\t22\t23\t24\t| |\t', self.black.free)
        
        print('__________________________________________________________', end = '')
        print('__________________________________________________________________')
        print('____BLACK = x_____________________________________________', end = '')
        print('________________________________________x HOME BOARD______________')

        
        return
    
    