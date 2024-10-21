import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(a, b) :

    visited[a][b] = True
    current_color = graph[a][b]

    for next in range(4):
        ny = a + dy[next]
        nx = b + dx[next]
        
        if 0<= nx < n and 0<= ny < n and visited[ny][nx] == False :
            if graph[ny][nx] == current_color :
                dfs(ny,nx)

n = int(input().rstrip())

graph = [list(input().rstrip()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

# 적록색약 x
result1, result2 = 0,0

for i in range(n):
    for j in range(n):
        if not visited[i][j] :
            dfs(i,j)
            result1+=1

# 적록색약 o 
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j] :
            dfs(i,j)
            result2 += 1

print(result1, result2)