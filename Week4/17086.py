import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

q = []
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, -1, 0, 1, -1, 1, -1, 1]

for i in range(m):
    for j in range(n):
        if graph[j][i] == 1:
            heapq.heappush(q, (0, j, i))

while q:
    r, j, i = heapq.heappop(q)
    for k in range(8):
        nx = dx[k] + i
        ny = dy[k] + j
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
            graph[ny][nx] = r + 1
            heapq.heappush(q, (r+1, ny, nx))
            
for k in range(len(graph)):
    ans = max(max(graph[k]), ans)
print(ans)