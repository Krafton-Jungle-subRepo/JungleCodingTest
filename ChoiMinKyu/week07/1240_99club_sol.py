# 빠른 입력을 위해 sys.stdin 사용
import sys
input = sys.stdin.readline
# deque 사용
from collections import deque

# bfs를 이용 해 문제 해결
def find_distance(start,end):
    queue = deque([(start,0)])
    visited = [False]*(N+1)
    visited[start] = True

    while queue:
        node, dist = queue.popleft()
        
        if node == end:
            return dist
        
        for next_node, next_dist in graph[node]:
            if not visited[next_node]:
                queue.append((next_node,dist+next_dist))
                visited[next_node] = True
                
# 입력 처리
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))
for _ in range(M):
    a, b = map(int, input().split())
    result = find_distance(a, b)
    print(result)
