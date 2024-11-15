# 문제집
import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

for _ in range(M):
    first, last = map(int, input().split())
    graph[first].append(last)
    degree[last] += 1

queue = []
for i in range(1, N + 1):
    if degree[i] == 0:
        heapq.heappush(queue, i)

result = []
while queue:
    current = heapq.heappop(queue)
    result.append(current)
    
    for next_node in graph[current]:
        degree[next_node] -= 1
        if degree[next_node] == 0:
            heapq.heappush(queue, next_node)

print(' '.join(map(str, result)))
