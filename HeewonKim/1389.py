# 케빈 베이컨의 6단계 법칙
import sys

N, M = map(int, sys.stdin.readline().split())
edges = [([sys.maxsize] * (N+1)) for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    edges[node1][node2] = 1
    edges[node2][node1] = 1

def floyd():
    for via in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                edges[i][j] = min(edges[i][j], edges[i][via] + edges[via][j])

floyd()
res = sys.maxsize
residx = -1
for i in range(1, N+1):
    if(res > sum(edges[i][1:])):
        res = sum(edges[i][1:])
        residx = i
print(residx)