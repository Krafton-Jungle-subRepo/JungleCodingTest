# 2048 (Easy)
import sys
from collections import deque

N = int(sys.stdin.readline())
Board = [(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
res = 0

def MoveBoard(direction, board):
    global res

    if(direction == 'L'):
        for y in range(N):
            queue = deque()
            for x in range(len(board[y])):
                if(board[y][x] != 0):
                    queue.append(board[y][x])
            tmp = []
            prevpop = -1
            while(queue):
                popped = queue.popleft()
                if(prevpop != popped):
                    if(prevpop != -1):
                        tmp.append(prevpop)
                    prevpop = popped
                else:
                    tmp.append(popped * 2)
                    prevpop = -1
            if(prevpop != -1):
                tmp.append(prevpop)
            for _ in range(N - len(tmp)):
                tmp.append(0)

            for i in range(N):
                board[y][i] = tmp[i]
                res = max(res, tmp[i])
                if(res == 512):
                    print("!!!!")

    elif(direction == 'U'):
        for x in range(N):
            queue = deque()
            for y in range(len(board[x])):
                if(board[y][x] != 0):
                    queue.append(board[y][x])
            tmp = []
            prevpop = -1
            while(queue):
                popped = queue.popleft()
                if(prevpop != popped):
                    if(prevpop != -1):
                        tmp.append(prevpop)
                    prevpop = popped
                else:
                    tmp.append(popped * 2)
                    prevpop = -1
            if(prevpop != -1):
                tmp.append(prevpop)
            
            for _ in range(N - len(tmp)):
                tmp.append(0)
            for i in range(N):
                board[i][x] = tmp[i]
                res = max(res, tmp[i])
                if(res == 512):
                    print("!!!!")
    
    elif(direction == 'R'):
        for y in range(N):
            queue = deque()
            for x in range(len(board[y])-1, -1, -1):
                if(board[y][x] != 0):
                    queue.append(board[y][x])
            tmp = []
            prevpop = -1
            while(queue):
                popped = queue.popleft()
                if(prevpop != popped):
                    if(prevpop != -1):
                        tmp.append(prevpop)
                    prevpop = popped
                else:
                    tmp.append(popped * 2)
                    prevpop = -1
            if(prevpop != -1):
                tmp.append(prevpop)
            
            for i in range(len(tmp)):
                board[y][N-1-i] = tmp[i]
                res = max(res, tmp[i])
                if(res == 512):
                    print("!!!!")
            for i in range(N - len(tmp)):
                board[y][i] = 0

    else:
        for x in range(N):
            queue = deque()
            for y in range(len(board[x])-1, -1, -1):
                if(board[y][x] != 0):
                    queue.append(board[y][x])
            tmp = []
            prevpop = -1
            while(queue):
                popped = queue.popleft()
                if(prevpop != popped):
                    if(prevpop != -1):
                        tmp.append(prevpop)
                    prevpop = popped
                else:
                    tmp.append(popped * 2)
                    prevpop = -1
            if(prevpop != -1):
                tmp.append(prevpop)
            
            for i in range(len(tmp)):
                board[N-1-i][x] = tmp[i]
                res = max(res, tmp[i])
                if(res == 512):
                    print("!!!!")
            for i in range(N - len(tmp)):
                board[i][x] = 0

def DFS(board, count, movelog):
    if(count >= 5):
        return
    
    tmpboard = [row[:] for row in board]
    MoveBoard('R', tmpboard)
    tmpmovelog = movelog[:]
    tmpmovelog.append('R')
    DFS(tmpboard, count+1, tmpmovelog)

    tmpboard = [row[:] for row in board]
    MoveBoard('L', tmpboard)
    tmpmovelog = movelog[:]
    tmpmovelog.append('L')
    DFS(tmpboard, count+1, tmpmovelog)

    tmpboard = [row[:] for row in board]
    MoveBoard('U', tmpboard)
    tmpmovelog = movelog[:]
    tmpmovelog.append('U')
    DFS(tmpboard, count+1, tmpmovelog)

    tmpboard = [row[:] for row in board]
    MoveBoard('D', tmpboard)
    tmpmovelog = movelog[:]
    tmpmovelog.append('D')
    DFS(tmpboard, count+1, tmpmovelog)

DFS(Board, 0, [])
print(res)