import sys
sys.setrecursionlimit(2500)  # 재귀 깊이 제한 증가
input = sys.stdin.readline
INF = sys.maxsize

answer = 0
# 상/하/좌/우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
directions = {'U':0,'D':1,'L':2,'R':3}

def dfs(px,py):
  global answer
  visited[px][py] = 1
  dir = directions[maze[px][py]]
  nx = px+dx[dir]
  ny = py+dy[dir]

  # 미로 밖으로 나가는 경우
  if nx <0 or nx >= N or ny < 0 or ny>=M:
    done[px][py] = 1
    return
  
  # 이미 처리가 완료된 경우
  if done[nx][ny]:
    done[px][py] = 1
    return
  
  # 순환이 발생한 경우
  elif visited[nx][ny]:
    sx = nx
    sy = ny
    tmp = INF
    while True:
      tmp = min(tmp,cost[sx][sy])
      d = directions[maze[sx][sy]]
      sx = sx+dx[d]
      sy = sy+dy[d]

      if sx == nx and sy==ny:
        break
    answer += tmp
  
  else:
    dfs(nx,ny)
  
  done[px][py] = 1


# 가로 M칸,세로 N칸
N, M = map(int,input().split())
maze = [input().rstrip() for _ in range(N)]
cost = [list(map(int,input().split())) for _ in range(N)]
done = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for i in range(N):
  for j in range(M):
    if not done[i][j]:
      dfs(i,j)

print(answer)