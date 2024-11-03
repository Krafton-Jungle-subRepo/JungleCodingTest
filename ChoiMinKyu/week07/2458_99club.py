import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int,input().split())

height = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    height[a][b] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if height[i][j] == 1 or (height[i][k] == 1 and height[k][j] == 1):
                height[i][j] = 1

answer = 0
for i in range(1,N+1):
    tmp = 0
    for j in range(N+1):
        if height[i][j] != INF or height[j][i] != INF:
            tmp += 1
    if tmp == N-1:
        answer += 1

print(answer)