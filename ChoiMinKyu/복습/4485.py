from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

def bfs(N):
  cost = [[INF]*N for _ in range(N)]
  cost[0][0] = graph[0][0]
  queue = deque([(0,0)])

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<N and 0<=ny<N:
        ncost = cost[x][y] + graph[nx][ny]
        if ncost < cost[nx][ny]:
          cost[nx][ny] = ncost
          queue.append((nx,ny))

  return cost[N-1][N-1]

N = -1
idx = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while (1):
  N = int(input())
  if N == 0:
    break
  graph = [list(map(int,input().split())) for _ in range(N)]
  answer = bfs(N)

  print(f"Problem {idx}: {answer}")
  idx+=1