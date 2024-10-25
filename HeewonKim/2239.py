# 스도쿠
import sys

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
ZeroIdx = []
for i in range(9):
   for j in range(9):
       if board[i][j] == 0:
           ZeroIdx.append((j, i))

def CheckSector(x, y, num):
    boardX =x // 3 * 3
    boardY = y // 3 * 3
    for i in range(boardY, boardY + 3):
        for j in range(boardX, boardX + 3):
            if board[i][j] == num:
                return False
    return True

def CheckRow(y, num):
    for i in range(9):
        if board[y][i] == num:  
            return False
    return True
    

def CheckColumn(x, num):
    for i in range(9):
        if num == board[i][x]:
            return False
    return True

def DFS(idx):
    if idx == len(ZeroIdx):
        for i in range(9):
            print(''.join(map(str, board[i])))
        exit(0)

    for i in range(1, 10):
        x = ZeroIdx[idx][0]
        y = ZeroIdx[idx][1]

        if CheckRow(y, i) and CheckColumn(x, i) and CheckSector(x, y, i):
            board[y][x] = i
            DFS(idx+1)
            board[y][x] = 0

DFS(0)
