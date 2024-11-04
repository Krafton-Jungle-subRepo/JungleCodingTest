# 키 순서
import sys

N, M = map(int, sys.stdin.readline().split())
edges = [([0] * (N+1)) for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    edges[start][end] = 1


for i in edges:
    print(i)

def floyd():
    for via in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if edges[i][via] and edges[via][j]:  
                    edges[i][j] = 1  
floyd()
for i in edges:
    print(i)