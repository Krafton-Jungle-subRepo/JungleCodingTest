import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def burn() :
    while queue :
        x, y, t = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w :
                if graph[nx][ny] != '#' and visited[nx][ny] == 0 :
                    visited[nx][ny] = t + 1
                    queue.append([nx, ny, t+1])
    
    return visited

def bfs(x, y) :
    q = deque()
    q.append([x, y, 1])

    while q : 
        cx, cy, t = q. popleft()

        if cx == 0 or cx == h -1 or cy == 0 or cy == w - 1 :
            return t
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < h and 0 <= ny < w :
                if graph[nx][ny] != '#' :
                    if visit[nx][ny] > t + 1 and visit[nx][ny] != -1 or visited[nx][ny] == 0 :
                        q.append([nx,ny, t+1])
                        visit[nx][ny] = -1

    return 'IMPOSSIBLE'

for _ in range(int(input())):
    w, h = map (int, input().split())
    graph = [list(map(str, input().rstrip())) for _ in range(h)]

    # 불이 붙은 위치 담을 큐
    queue = deque()
    visited = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w) :
            # 해당 구역에 불이 붙으면 큐에 좌표 삽입
            if graph[i][j] == '*' :
                queue.append([i, j, 1])
                visited[i][j] = 1
            elif graph[i][j] == '@':
                sx, sy = i, j
    
    visit = burn()

    print(bfs(sx, sy))