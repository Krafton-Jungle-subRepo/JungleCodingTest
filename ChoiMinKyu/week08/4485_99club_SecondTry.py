# import deque
from collections import deque
# 빠른 입력을 위해 stdin 사용
import sys
input = sys.stdin.readline
# system의 maxsize를 INF로 사용
INF = sys.maxsize

# bfs로 구현
def bfs(N):
    cost = [[INF]*N for _ in range(N)]
    cost[0][0] = graph[0][0]
    queue = deque([(0,0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                ncost = cost[x][y] + graph[nx][ny]
                if ncost < cost[nx][ny]:
                    cost[nx][ny] = ncost
                    queue.append((nx,ny))
    
    return cost[N-1][N-1]

# 상,하,좌,우를 표시할 delta X, delta Y
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = -1 # N으로 테스트 케이스 조절
idx = 1 # 결과 출력을 위한 인덱스
while(1):
    # N값 입력 (0이면 종료)
    N = int(input())
    if N == 0:
        break
    # 그래프 입력
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    # bfs 함수 호출
    result = bfs(N)
    # 결과 출력 후 idx + 1
    print(f"Problem {idx}: {result}")
    idx += 1