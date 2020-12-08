import pygame
import numpy as np
from player import Player
from board import Board
import time

BLACK = -1
WHITE = 1
BAR = 0

# Init game
white = Player(1)
black = Player(-1,)
white.opponent = black
black.opponent = white
board = Board(white,black)

# Init pygame
pygame.init()

# Make the screen
screen = pygame.display.set_mode((1650,827))
#Title
pygame.display.set_caption('Backgammon')
# Icon
icon = pygame.image.load('dice.png')
pygame.display.set_icon(icon)
# Background
background = pygame.image.load('board.jpg')
# Token images
white_token = pygame.image.load('white_dot.png')
black_token = pygame.image.load('black_dot2.png')
# Dice images
one = pygame.image.load('inverted-dice-1.png')
two = pygame.image.load('inverted-dice-2.png')
three = pygame.image.load('inverted-dice-3.png')
four = pygame.image.load('inverted-dice-4.png')
five = pygame.image.load('inverted-dice-5.png')
six = pygame.image.load('inverted-dice-6.png')
# Font style
myfont = pygame.font.SysFont("Helvetica", 30)
cp_label = myfont.render('Current Player: ',2, (0,0,0))
pm_label = myfont.render('Possible Moves: ',2,(0,0,0))

pm_font = pygame.font.SysFont('Helvetica', 15)

current_player = white
i = 0
# DICE roll
def roll_dice():
    dices = np.random.randint(1,7,2)
    if dices[0] == dices[1]:
        return np.array([dices[0], dices[1], dices[1], dices[1]])
    return dices

def white_token_at(coord_x,coord_y):
    screen.blit(white_token,(coord_x,coord_y))

def black_token_at(coord_x,coord_y):
    screen.blit(black_token,(coord_x,coord_y))

def dice_display(img, coord_x,coord_y):
    screen.blit(img,(coord_x,coord_y))


y1_12 = 18
y13_24 = 717
board_coords = np.zeros(25, dtype=int)
board_coords[1] = 33+88+89+89+90+87+116+88+88+89+89+89
board_coords[2] = 33+88+89+89+90+87+116+88+88+89+89
board_coords[3] = 33+88+89+89+90+87+116+88+88+89
board_coords[4] = 33+88+89+89+90+87+116+88+88
board_coords[5] = 33+88+89+89+90+87+116+88
board_coords[6] = 33+88+89+89+90+87+116
board_coords[7] = 33+88+89+89+90+87
board_coords[8] = 33+88+89+89+90
board_coords[9] = 33+88+89+89
board_coords[10] = 33+88+89
board_coords[11] = 33+88
board_coords[12] = 33
board_coords[13] = 33
board_coords[14] = 33+88
board_coords[15] = 33+88+89
board_coords[16] = 33+88+89+89
board_coords[17] = 33+88+89+89+90
board_coords[18] = 33+88+89+89+90+87
board_coords[19] = 33+88+89+89+90+87+116
board_coords[20] = 33+88+89+89+90+87+116+88
board_coords[21] = 33+88+89+89+90+87+116+88+88
board_coords[22] = 33+88+89+89+90+87+116+88+88+89
board_coords[23] = 33+88+89+89+90+87+116+88+88+89+89
board_coords[24] = 33+88+89+89+90+87+116+88+88+89+89+89

running = True

# Game loop
while not white.is_done() and not black.is_done():
    # current player roll the dice
    current_player.dices = roll_dice()
    current_player.all_dices = current_player.dices
    #current_player playes
    while (current_player.dices.size is not 0):
        
        
        
    

        #GUI----------------------------------------
        # RBG
        screen.fill(0xFFFFFF)
        
        # Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        screen.blit(background,(0,0))
        pygame.draw.rect(screen,(0,0,0),[0,0,1650,20])
        pygame.draw.rect(screen,(0,0,0),[0,827-20,1650,20])
        pygame.draw.rect(screen,(0,0,0),[0,0,20,1550])
        pygame.draw.rect(screen,(0,0,0),[1650-20,0,20,827])
        pygame.draw.rect(screen,(0,0,0),[1169/2-10,0,20,827])
        pygame.draw.rect(screen,(0,0,0),[1169-25,0,20,827])
        # Board tokens
        for i in range(0,25,1):
            if board.board[i] > 0:
                if i < 13:
                    for j in range(0,board.board[i],1):
                        if j < 5:
                            y = y1_12+60*j
                        else:
                            y = y1_12+20+60*(j-5)
                        white_token_at(board_coords[i],y)
                else:
                    for j in range(0,board.board[i],1):
                        if j < 5:
                            y = y13_24-60*j
                        else:
                            y = y13_24-20-60*(j-5)
                        white_token_at(board_coords[i],y)
            elif board.board[i] < 0:
                if i < 13:
                    for j in range(0,-board.board[i],1):
                        if j < 5:
                            y = y1_12+60*j
                        else:
                            y = y1_12+20+60*(j-5)
                        black_token_at(board_coords[i],y)
                else:
                    for j in range(0,-board.board[i],1):
                        if j < 5:
                            y = y13_24-60*j
                        else:
                            y = y13_24-20-60*(j-5)
                        black_token_at(board_coords[i],y)
        # Bar tokens
        if white.bar > 0:
            for k in range(0,white.bar,1):
                white_token_at(33+88+89+89+90+87+116/2, 330-40*k)
        if black.bar > 0:
            for k in range(0,black.bar,1):
                black_token_at(33+88+89+89+90+87+116/2, 400+40*k)

        # Free tokens
        if white.free > 0:
            for k in range(0,white.free,1):
                white_token_at(1150, y1_12+15*k)
        if black.free > 0:
            for k in range(0,black.free,1):
                black_token_at(1150, y13_24-15*k)

        # Dice 
        for d in range(0,2):
            if current_player.all_dices[d] == 1:
                dice_display(one,1230, 300+130*d)
            elif current_player.all_dices[d] == 2:
                dice_display(two,1230, 300+130*d)
            elif current_player.all_dices[d] == 3:
                dice_display(three,1230, 300+130*d)
            elif current_player.all_dices[d] == 4:
                dice_display(four,1230, 300+130*d)
            elif current_player.all_dices[d] == 5:
                dice_display(five,1230, 300+130*d)
            elif current_player.all_dices[d] == 6:
                dice_display(six,1230, 300+130*d)

        # Text
        screen.blit(cp_label, (1240, 40))
        if current_player == white:
            player_label = myfont.render('WHITE',3,(0,0,0))
        else:
            player_label = myfont.render('BLACK',3,(0,0,0))
        screen.blit(player_label, (1480,40))
        screen.blit(pm_label,(1340, 100))

        if current_player.color == WHITE:
            current_player.home = sum(board.board[1:7][board.board[1:7]>0])
        elif current_player.color == BLACK:
            current_player.home = sum(board.board[19:25][board.board[19:25]<0])
        
        
        current_player.possible_moves(board.board)

        # Display possible moves
        m = 0
        for nbr, p in enumerate(current_player.moves):
            pm_str = f"[{nbr}]  -> " + "From " + str(p[0]) + " with " + str(p[1]) + " to " + str(p[2])
            pm_label = pm_font.render(pm_str,2, (0,0,0))
            screen.blit(pm_label,(1340,130+20*m))
            m+=1
        pm_label = myfont.render('Possible Moves: ',2,(0,0,0))

        pygame.display.update()
        if not running:
            break
        #time.sleep(0.2)

        if i == 7: break

        # current_player moves a token
        if len(current_player.moves) > 0:
            #move_nbr = np.random.randint(0,len(current_player.moves))
            move_nbr = -1
            while move_nbr == -1 or move_nbr > len(current_player.moves)-1:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            move_nbr = 0
                        if event.key == pygame.K_1:
                            move_nbr = 1
                        if event.key == pygame.K_2:
                            move_nbr = 2
                        if event.key == pygame.K_3:
                            move_nbr = 3
                        if event.key == pygame.K_4:
                            move_nbr = 4
                        if event.key == pygame.K_5:
                            move_nbr = 5
                        if event.key == pygame.K_6:
                            move_nbr = 6
                        if event.key == pygame.K_7:
                            move_nbr = 7
                        if event.key == pygame.K_8:
                            move_nbr = 8
                        if event.key == pygame.K_9:
                            move_nbr = 9


            #move_nbr = int(input())

            # move one token
            board.move(current_player.moves[move_nbr][0],current_player.moves[move_nbr][1],current_player) 
            # remove the used dice
            current_player.dices = np.delete(current_player.dices,np.where(current_player.dices == current_player.moves[move_nbr][1])[0][0])
        else:
            current_player.dices = np.array([])

        
    current_player = current_player.opponent

while running:
    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    