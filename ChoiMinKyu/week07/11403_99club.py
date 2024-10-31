# 빠른 입력을 위해 stdin사용
import sys
input = sys.stdin.readline

# 정점 개수 N
N = int(input())

# 그래프 입력
G = [list(map(int,input().split())) for _ in range(N)]

# 거쳐갈 노드 k에 대해
for k in range(N):
    # 세로축, 가로축을 기준으로 반복하면서
    for i in range(N):
        for j in range(N):
            # 바로 갈 수 있거나, k를 거쳐 갈 수 있는 노드에 대해
            if G[i][j]>0 or G[i][k]>0 and G[k][j] > 0:
                # 그래프 배열에 기록
                G[i][j] = 1
# 결과 출력
for i in range(N):
    print(' '.join(map(str,G[i])))