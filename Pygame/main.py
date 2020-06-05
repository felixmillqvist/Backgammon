import numpy as np
from player import Player
from board import Board
BLACK = -1
WHITE = 1
BAR = 0


white = Player(1)
black = Player(-1,)
white.opponent = black
black.opponent = white
board = Board(white,black)

current_player = white
i = 0

def roll_dice():
    dices = np.random.randint(1,7,2)
    if dices[0] == dices[1]:
        return np.array([dices[0], dices[1], dices[1], dices[1]])
    return dices

board.print()

while not white.is_done() and not black.is_done():
    i = i+1
    
    # current player roll the dice
    current_player.dices = roll_dice()
 

    #current_player playes
    while (current_player.dices.size is not 0):
        if i == 7: break
        print('Current Player:\t', 'WHITE - o' if current_player.color == 1 else 'BLACK - x')

        print('Dice rolled:\t', end = '')
        for die in current_player.dices:
            print(die, end = '\t')
        print()
        
        if current_player.color == WHITE:
            current_player.home = sum(board.board[1:7][board.board[1:7]>0])
        elif current_player.color == BLACK:
            current_player.home = sum(board.board[19:25][board.board[19:25]<0])
        
        
        current_player.possible_moves(board.board)
        
        print(current_player.moves)
        #print(current_player.possible_moves(board.board))
        # current_player moves a token
        if len(current_player.moves) > 0:
            move_nbr = np.random.randint(0,len(current_player.moves))
            print(current_player.moves[move_nbr])
            # move one token
            board.move(current_player.moves[move_nbr][0],current_player.moves[move_nbr][1],current_player) 
            # remove the used dice
            current_player.dices = np.delete(current_player.dices,np.where(current_player.dices == current_player.moves[move_nbr][1])[0][0])
        else:
            current_player.dices = np.array([])

        board.print()
        
        
    current_player = current_player.opponent
print(i)    
print('Winner is:\t', 'WHITE - o' if current_player.opponent.color == 1 else 'BLACK - x')    
    