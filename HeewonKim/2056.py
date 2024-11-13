# 작업
import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
cost = [0] * (N+1)
degree = [0] * (N+1)
queue = deque()
res = [0] * (N+1)

for i in range(1, N+1):
    inputarr = list(map(int, sys.stdin.readline().split()))
    cost[i] = inputarr[0]
    for j in range(inputarr[1]):
        arr[inputarr[2+j]].append(i)
    degree[i] += inputarr[1]
    if(degree[i] == 0):
        queue.append(i)
        res[i] = cost[i]
        
while(queue):
    popped = queue.popleft()
    for i in range(len(arr[popped])):
        next = arr[popped][i]
        res[next] = max(res[next], res[popped] + cost[next])
        degree[next] -= 1
        if(degree[next] == 0):
            queue.append(next)

print(max(res))