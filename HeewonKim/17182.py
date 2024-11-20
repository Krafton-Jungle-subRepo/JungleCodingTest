# 우주 탐사선
import sys
N, K = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for via in range(N):
    for i in range(N):
        for j in range(N):
            edges[i][j] = min(edges[i][j], edges[i][via] + edges[via][j])

def Dfs(node, visited, costs):
    global total
    if(costs >= total):
        return
    else:
        if(False not in visited):
            total = costs
            return

    for i in range(N):
        if(not visited[i]):
            visited[i] = True
            Dfs(i, visited, costs + edges[node][i])
            visited[i] = False

total = sys.maxsize
visited = [False] * N
visited[K] = True
Dfs(K, visited, 0)
print(total)