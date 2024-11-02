import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y,height) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q :
        cx, cy = q.popleft()
        
        for next in range(4):
            nx = cx + dx[next]
            ny = cy + dy[next]

            if 0<= nx < n and 0<= ny < n and graph[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

n = int(input())

max_num = 0
graph = []

for _ in range(n):
    low = list(map(int, input().split()))
    graph.append(low)
    
    max_num = max(low)

# result = []
answer = 0

# 1부터 최대 높이까지 순회한다.
for i in range(max_num) :
    count = 0
    visited = [[False] * n for _ in range(n)]   
    for j in range(n):
        for k in range(n):
            # 방문하지 않고 구역의 높이가 잠긴 높이보다 클 경우.
            if not visited[j][k] and graph[j][k] > i :
                bfs(j,k,i)
                # 안전영역 count
                count += 1
            
    # count의 최대값 설정.
    answer = max(count, answer)
    # result.append(count)

print(answer)