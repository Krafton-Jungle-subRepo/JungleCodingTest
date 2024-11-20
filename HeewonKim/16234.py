# 인구 이동
import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(start_x, start_y, visited):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_y][start_x] = True
    
    union = [(start_x, start_y)]  # 연합에 포함된 국가들
    total_population = board[start_y][start_x]
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                # 국경을 열 수 있는 조건
                if L <= abs(board[y][x] - board[ny][nx]) <= R:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_population += board[ny][nx]
                    count += 1

    # 연합에 포함된 국가들의 인구를 재분배
    new_population = total_population // count
    for x, y in union:   
        board[y][x] = new_population
    
    return count > 1  # 연합이 형성되었는지 여부 반환


def check_area():
    visited = [[False] * N for _ in range(N)]
    is_moved = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                # 연합을 형성하고 이동 여부를 체크
                if bfs(j, i, visited):
                    is_moved = True
    
    return is_moved


result = 0
while True:
    if not check_area():
        break
    result += 1
print(result)
