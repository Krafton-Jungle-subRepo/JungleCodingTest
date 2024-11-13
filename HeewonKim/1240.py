# 노드사이의 거리
import sys
N, M = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    node1, node2, cost = map(int, sys.stdin.readline().split())
    edges[node1].append([node2, cost])
    edges[node2].append([node1, cost])

def dfs(current, end, count, visited):
    if(current == end):
        return count
    result = -1
    for i in range(len(edges[current])):
        if(edges[current][i][0] not in visited):
            visited.append(edges[current][i][0])
            result = dfs(edges[current][i][0], end, count+edges[current][i][1], visited)
            if(result != -1):
                return result
    return result


for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    visited = [start]
    print(dfs(start, end, 0, visited))