# 내리막 길

import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1] * M for _ in range(N)]  # 메모이제이션 배열 초기화 (-1은 아직 계산 안 된 상태를 의미)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def Dfs(currentX, currentY):
    # 목표 지점에 도달한 경우
    if currentX == M - 1 and currentY == N - 1:
        return 1
    
    # 이미 계산된 경로 수가 있다면 그 값을 반환
    if dp[currentY][currentX] != -1:
        return dp[currentY][currentX]

    # 현재 위치에서 출발하는 경로의 수를 0으로 초기화
    dp[currentY][currentX] = 0

    # 4방향 탐색
    for i in range(4):
        nextX = currentX + dx[i]
        nextY = currentY + dy[i]

        # 다음 위치가 범위 내에 있고, 내리막길 조건을 만족하는 경우
        if 0 <= nextX < M and 0 <= nextY < N and board[currentY][currentX] > board[nextY][nextX]:
            dp[currentY][currentX] += Dfs(nextX, nextY)

    return dp[currentY][currentX]

# (0, 0)에서 DFS 시작
print(Dfs(0, 0))
