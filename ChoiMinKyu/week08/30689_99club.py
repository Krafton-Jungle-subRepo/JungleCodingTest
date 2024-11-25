import sys
sys.setrecursionlimit(2500)  # 재귀 깊이 제한 증가

# 방향 설정
dy = [1, -1, 0, 0]  # 아래, 위, 오른쪽, 왼쪽
dx = [0, 0, 1, -1]
m = {'U': 1, 'D': 0, 'L': 3, 'R': 2}  # 방향 매핑

# 변수 초기화
N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
cost = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
done = [[0] * M for _ in range(N)]
answer = 0

# DFS 함수 정의
def dfs(py, px):
    global answer
    visited[py][px] = 1
    dir = m[arr[py][px]]
    y, x = dy[dir] + py, dx[dir] + px
    
    # 미로 밖으로 나가는 경우
    if x < 0 or y < 0 or x >= M or y >= N:
        done[py][px] = 1
        return
    
    if done[y][x]:  # 이미 처리가 완료된 칸인 경우
        done[py][px] = 1
        return
    elif visited[y][x]:  # 순환이 발생한 경우 (사이클 탐지)
        sy, sx = y, x
        cc = float('inf')
        while True:
            cc = min(cc, cost[sy][sx])
            d = m[arr[sy][sx]]
            sy, sx = dy[d] + sy, dx[d] + sx
            if sy == y and sx == x:
                break
        answer += cc
    else:
        dfs(y, x)
    
    done[py][px] = 1

# 모든 칸에 대해 DFS 수행
for i in range(N):
    for j in range(M):
        if not done[i][j]:
            dfs(i, j)

# 결과 출력
print(answer)
