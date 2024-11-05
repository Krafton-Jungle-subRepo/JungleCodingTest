import sys
from copy import deepcopy
input = sys.stdin.readline

from collections import deque

# 빙산 주위 물의 개수 세기
def melt_ice(y,x):
    count = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < m and 0 <= ny < n and graph_copy[ny][nx] == 0 :
            count += 1
    
    return count
    
def check_iceberg(y,x):
    q = deque()
    q.append((y,x))
    visited[y][x] = True

    while q :
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny < n and 0<=nx < m and not visited[ny][nx] and graph[ny][nx] != 0  :
                visited[ny][nx] = True
                q.append((ny,nx))


n , m = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

# 시간(년)변수
result = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while True:
    # 첫 빙산 유무, 없으면 -1을 반환하고 끝낸다.
    flag = True

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                flag = False

    if flag :
        print(0)
        break

    # 방문 여부 리스트 만든다.
    visited = [[False] * m for _ in range(n)]
    # 빙산 개수 
    piece = 0

    # 빙산 녹이기
    graph_copy = deepcopy(graph)
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph_copy[i][j] != 0 :
                graph[i][j] = max(0, graph[i][j] - melt_ice(i,j))

    # 나누어진 빙산 개수 구하기
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j] and graph[i][j] != 0:
                check_iceberg(i,j)
                piece += 1
    
    # 빙산 개수가 2개 이상이면 그때의 시간 출력
    if piece >= 2 :
        print(result)
        break

    result += 1