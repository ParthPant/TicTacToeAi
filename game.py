import pygame, sys
from math import inf

pygame.init()

size = 500
running = True
screen = pygame.display.set_mode((size, size))
spriteSize = 16
winner = 0
availabeMoves = []
human = 'O'
ai = 'X'
player = ai

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
                        
def checkWinner(board):
    winner =0 
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1] == board[i][2]:
            winner = board[i][0]
            return winner

    for i in range(3):
        if board[0][i]==board[1][i] and board[1][i] == board[2][i]:
            winner = board[0][i]
            return winner

    if (board[0][0]== board[1][1]) and (board[1][1]==board[2][2]):
        winner = (board[0][0])
    if (board[0][2]== board[1][1]) and (board[1][1]==board[2][0]):
        winner = (board[0][2])

    if (winner == '') and len(availabeMoves) == 0:
        winner = 'tie'

    return winner

def getAiMove(board):
    maxScore = float(-inf)
    optimMove = ()
    scores = []
    for i, row in enumerate(board):
        for j,box in enumerate(row):
            if (box == 0):
                board[i][j] = ai
                #minimax
                score = minimax(board, 0, False)
                board[i][j] = 0
                scores.append(score)
                if score > maxScore:
                    maxScore = score
                    optimMove = (i,j)

    print(scores)
    return optimMove 

def minimax(board, depth, isMaximising):
    result = checkWinner(board)
    if result:
        if result== ai:
            return 10  
        elif result == human:
            return -10
        elif result == 'tie':
            return 0
        
    if (isMaximising):
        bestScore = float(-inf)
        for i, row in enumerate(board):
            for j,box in enumerate(row):
                if board[i][j] == 0:
                    board[i][j] = ai
                    score = minimax(board,depth+1, False)
                    board[i][j] = 0
                    bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = float(inf)
        for i, row in enumerate(board):
            for j,box in enumerate(row):
                if board[i][j] == 0:
                    board[i][j] = human
                    score = minimax(board, depth+1, True)
                    board[i][j] = 0
                    bestScore = min(bestScore, score)
        return bestScore
        

def getAvailableMoves(board):
    availabeMoves = []
    for i, row in enumerate(board):
        for j,box in enumerate(row):
            if board[i][j] == 0:
                availabeMoves.append((i,j))

    return availabeMoves

screen.fill((255,255,255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and player == human:
                (x, y) = pygame.mouse.get_pos()
                if x < size and y < size and x > 0 and y > 0:
                    (i, j) = getBoxNumber(x, y)
                    if board[i][j] == 0:
                        board[i][j] = human
                        player = ai
                        availabeMoves = getAvailableMoves(board)
                        winner = checkWinner(board)

    if(not winner and player == ai):
        (i, j) = getAiMove(board)
        board[i][j] = ai
        player = human
        winner = checkWinner(board)
                        
    if winner:
        print('winner is {}'.format(winner))
        # sys.exit();
    
    drawBoard()
    pygame.display.flip()

