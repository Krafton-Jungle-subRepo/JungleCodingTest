# 트리와 쿼리
import sys
sys.setrecursionlimit(10**5)

N, R, Q = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int, sys.stdin.readline().split())
    edge[start].append(end)
    edge[end].append(start)

visited = [0] * (N+1)
visited[R] = 1

def DFS(Node):
    for i in range(len(edge[Node])):
        nextNode = edge[Node][i]
        if(visited[nextNode] == 0):
            visited[nextNode] = 1
            visited[Node] += DFS(nextNode) + visited[nextNode] 
    return 0

DFS(R)

for _ in range(Q):
    U = int(sys.stdin.readline())
    print(visited[U])