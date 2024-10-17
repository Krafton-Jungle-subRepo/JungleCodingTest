import sys
from collections import deque
input = sys.stdin.readline

def bfs(y,x):
    global count

    q = deque()
    q.append((y,x))

    while q:
        c_y, c_x = q.popleft()

        for next in range(4):
            n_y = c_y + dy[next]
            n_x = c_x + dx[next]

            if(0 <= n_y < n and 0 <= n_x < m and graph[n_y][n_x] == 1) :
                graph[n_y][n_x] =0
                q.append((n_y, n_x))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

t = int(input())
for _ in range(t):
    m, n, k = map(int,input().split())

    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int,input().split())
        graph[b][a] = 1


    count = 0



    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 1) :
                count += 1
                bfs(i,j)

    print(count)