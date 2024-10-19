# 음악프로그램
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

arcs = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for i in range(M):
    inputArr = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(inputArr)):
        for k in range(j+1, len(inputArr)):
            if(inputArr[k] not in arcs[inputArr[j]]):
                arcs[inputArr[j]].append(inputArr[k])
                degree[inputArr[k]] += 1

queue = deque()
res = []
for i in range(1, N+1):
    if(degree[i] == 0):
        queue.append(i)

while(queue):
    current = queue.popleft()
    res.append(current)
    for i in range(len(arcs[current])):
        next = arcs[current][i]
        degree[next] -= 1
        if(degree[next] == 0):
            queue.append(next)

if(len(res) != N):
    print(0)
else:
    print('\n'.join(map(str, res)))
