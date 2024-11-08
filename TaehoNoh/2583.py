import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    q = deque()
    q.append((x,y))

    cnt = 1

    while q :
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = 1
                    q.append((nx, ny))   
                    cnt += 1
    
    return cnt

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]

for _ in range(k):
    x1 , y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

res = []
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            graph[i][j] = 1
            res.append(bfs(i,j))


print(len(res))
print(*sorted(res))