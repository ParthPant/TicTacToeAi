import pygame, sys

pygame.init()

size = 500
running = True
screen = pygame.display.set_mode((size, size))
spriteSize = 16

crossImg = pygame.image.load('cross.png')
zeroImg = pygame.image.load('zero.png')

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

def getBoxNumber(x, y):
    i =0
    j = 0
    if x < size/3:
        j =0
    elif x < 2*size/3:
        j =1
    elif x < 3*size/3:
        j =2
   # ----------- 
    if y < size/3:
        i =0
    elif y < 2*size/3:
        i =1
    elif y < 3*size/3:
        i =2
   # ----------- 
    return (i,j)

def drawBoard():
    for i in range(3-1):
        n = (i+1)* size/3
        pygame.draw.lines(screen, (0,0,0), False, [(n, 0), (n, size)], 3)

    for i in range(3-1):
        n = (i+1)* size/3
        pygame.draw.lines(screen, (0,0,0), False, [(0, n), (size, n)], 3)

    for i,row in enumerate(board):
        for j,box in enumerate(row):
            box_center = ( ((size/6) + (j)*size/3)- spriteSize, ((size/6)
                + (i)*size/3)-spriteSize )
            if box == "O":
                screen.blit(zeroImg,box_center)
            if box == "X":
                screen.blit(crossImg,box_center)
                        
player = 'O'
screen.fill((255,255,255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                (x, y) = pygame.mouse.get_pos()
                if x < size and y < size and x > 0 and y > 0:
                    (i, j) = getBoxNumber(x, y)
                    if board[i][j] == 0:
                        board[i][j] = player
                        if player == 'O':
                            player = 'X'
                        else:
                            player = 'O'
                        #minimax logic here
    
    drawBoard()
    pygame.display.flip()

