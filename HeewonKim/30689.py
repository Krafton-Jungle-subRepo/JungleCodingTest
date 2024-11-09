# 미로 보수
import sys

sys.setrecursionlimit(10 ** 5) 
N, M = map(int, sys.stdin.readline().split())

directions = [list(sys.stdin.readline().strip()) for _ in range(N)]
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = {'R': 1, 'D': 0, 'L': -1, 'U': 0}
dy = {'R': 0, 'D': 1, 'L': 0, 'U': -1}

visited = [[0]*M for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            x, y = j, i
            path = []
            while True:
                if visited[y][x] == 2:
                    break 
                if visited[y][x] == 1:
                    cycle_start_index = path.index((x, y))
                    cycle_nodes = path[cycle_start_index:]
                    minCost = sys.maxsize
                    minX, minY = -1, -1
                    for cx, cy in cycle_nodes:
                        if costs[cy][cx] < minCost:
                            minCost = costs[cy][cx]
                            minX, minY = cx, cy
                    directions[minY][minX] = 'J'
                    result += minCost
                    break
                visited[y][x] = 1 
                path.append((x, y))
                dir_char = directions[y][x]
                if dir_char == 'J' or dir_char not in dx:
                    break  
                nx, ny = x + dx[dir_char], y + dy[dir_char]
                if not (0 <= nx < M and 0 <= ny < N):
                    break  
                x, y = nx, ny
            for px, py in path:
                visited[py][px] = 2

print(result)


