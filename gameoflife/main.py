import numpy as np
import os
from time import sleep

rows, cols = 10, 10
percentage = 0.4

def createBoard(rows, cols):
    board = []
    for x in range(0, cols):
        board.append([])
        for _ in range(0, rows):
            board[x].append('.')
    return board

def printBoard(board):
    for row in board:
        for item in row:
            print(item, end=' ')
        print()
    print()

def initBoard(board):
    for x in range(0, rows):
        for y in range(0, cols):
            if(np.random.rand() < percentage):
                board[x][y] = 'O'
    return board

def updateBoard(board):
    newBoard = createBoard(rows, cols)
    for x in range(0,cols):
        for y in range(0,rows):
            alive_neighbours = 0
            for nx in [-1, 0, 1]:
                for ny in [-1, 0, 1]:
                    if nx == 0 and ny == 0:
                        continue
                    new_x = x + nx
                    new_y = y + ny
                    if new_x >= 0 and new_x < rows and new_y >= 0 and new_y < cols:
                        if board[new_x][new_y] == 'O':
                            alive_neighbours += 1
            if board[x][y] == '.' and alive_neighbours == 3:
                newBoard[x][y] = 'O'
            elif board[x][y] == 'O' and (alive_neighbours == 2 or alive_neighbours ==3):
                newBoard[x][y] = 'O'
    return newBoard



board = createBoard(rows, cols)

board = initBoard(board)
# board[1][2] = 'O'
# board[1][3] = 'O'
# board[1][4] = 'O'

while True:
    printBoard(board)
    board = updateBoard(board)
    sleep(0.2)
    os.system('cls')