# 도시 분할 계획
import sys
import heapq
N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N+1)]
heap = []
res = 0

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, [cost, start, end])

def FindRoot(node):
    while(node != parent[node]):
        node = parent[node]
    return node

rank = [0] * (N+1)  

def CompareRoot(node1, node2):
    root1 = FindRoot(node1)
    root2 = FindRoot(node2)
    
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1
        return True
    return False


total = 0
lastCost = -1
while(heap):
    currentCost, currentStart, currentEnd = heapq.heappop(heap)
    if(CompareRoot(currentStart, currentEnd)):
        total += currentCost
        lastCost = currentCost

print(total - lastCost)