import numpy as np
BLACK = -1
WHITE = 1
BAR = 0
class Player:
    BLACK = -1
    WHITE = 1
    BAR = 0
    def __init__(self, color):
        self.color = color
        self.bar = 0
        self.free = 0
        self.home = 5
        self.moves = []
        self.dices = []
        self.all_dices = []
        self.opponent = None
        
    def bearing_off_possible(self):
        return (self.home + self.free) == 15 or (self.home - self.free) == -15
    
    def has_dead_piece(self):
        return self.bar > 0
    
    def increase_free(self):
        self.free += 1
        
    def decrease_free(self):
        self.free += -1
        
    def increase_bar(self):
        self.bar += 1
        
    def decrease_bar(self):
        self.bar += -1
        
    def increase_home(self):
        self.home += 1
    
    def decrease_home(self):
        self.home += -1
        
    def is_done(self):
        return self.free == 15
    
    def possible_moves(self, board):
        # move is based [from tongue number, with die, to tongue number]
        self.moves = []
        moves = []
        # go trough all dices
        for die in self.dices:
            
            if self.color == WHITE:
                #if dead piece
                if self.has_dead_piece(): 
                    print('has dead pieces, ', die)
                    if board[25-die] > -2:
                        moves.append([BAR, die, 25-die])
                    
                # if no dead pieces
                else:
                    # if all bearing off is possible
                    if self.bearing_off_possible():
                        print('bearing off possible')
                        if board[die] > 0:
                            moves.append([die,die, 'Bearing off'])
                        
                        elif not self.is_done():
                            other_possible_die = False;
                            for die_temp in self.dices:
                                other_possible_die = board[die_temp] > 0
                                if other_possible_die is True:
                                    break
                            if other_possible_die is False:
                                start_pip = np.max(np.where(board[1:7]>0))+1
                                if start_pip < die:
                                    moves.append([start_pip, die, 'Bearing off'])
                    
                    for start_pip in np.where(board[1:25]>0)[0]+1:
                        end_pip = start_pip-die
                        if end_pip > 0 and board[end_pip] > -2:
                            moves.append([start_pip,die, end_pip])
                        
            elif self.color == BLACK:
                #if dead piece
                if self.has_dead_piece():
                    print('has dead pieces, ',die)
                    if board[0+die] < 2:
                        
                        moves.append([BAR, die, 0+die])
                # if no dead pieces
                else:
                    # if all bearing off is possible
                    if self.bearing_off_possible():
                        print('bearing off possible')
                        if board[25-die] < 0:
                            moves.append([25-die,die, 'Bearing off'])
                        
                        elif not self.is_done():
                            other_possible_die = False;
                            for die_temp in self.dices:
                                other_possible_die = board[25-die_temp] < 0
                                if other_possible_die is True:
                                    break
                            if other_possible_die is False:
                                start_pip = np.min(np.where(board[19:25]<0))+19
                                if 25-start_pip < die:
                                    moves.append([start_pip, die, 'Bearing off'])
                    
                    for start_pip in np.where(board[1:25]<0)[0]+1:
                        end_pip = start_pip+die
                        if end_pip < 25 and board[end_pip] < 2:
                            moves.append([start_pip,die, end_pip])
        
            if len(self.dices) > 1 and self.dices[0] == self.dices[1]:
                break
        self.moves = moves
        return moves
    
    