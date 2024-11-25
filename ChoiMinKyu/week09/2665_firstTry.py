import sys
from collections import deque
input = sys.stdin.readline

INF = sys.maxsize

def sol(px,py):
  global answer

  queue = deque([(px,py)])
  visited[px][py] = 1
  cost[px][py] = int(rooms[px][py])

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
        ncost = cost[x][y] + int(rooms[nx][ny])
        if ncost < cost[nx][ny]:
          
          cost[nx][ny] = ncost
          visited[nx][ny] = 1
          queue.append((nx,ny))


N = int(input())
# 상. 하. 좌. 우.
dx = [-1,1,0,0]
dy = [0,0,-1,1]
rooms = [input().rstrip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cost = [[INF]*N for _ in range(N)]
answer = 0
sol(0,0)

print(cost)