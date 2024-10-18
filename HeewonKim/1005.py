# ACM Craft
import sys
from collections import deque

# 입력
T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    cost = list(map(int, sys.stdin.readline().split()))
    degree = [0] * (N+1)
    arcs = [[] for _ in range (N+1)]
    for i in range(K):
        start, end = map(int, sys.stdin.readline().split())
        arcs[start].append(end)
        degree[end] += 1
    W = int(sys.stdin.readline())

    # 큐, 결과 저장할 배열 선언    
    queue = deque()
    result = [0] * (N+1)
    # degree가 0일경우 큐에 삽입 및 결과값 저장
    for i in range(1, N+1):
        if(degree[i] == 0):
            queue.append(i)
            result[i] = cost[i-1]
    
    # 큐가 빌때까지 반복
    while(queue):
        currentNode = queue.popleft()
        # 다음 노드에 대해
        for i in range(len(arcs[currentNode])):
            # degree를 1 낮추고, 결과값 최신화
            next = arcs[currentNode][i]
            degree[next] -= 1 
            result[next] = max(result[next], result[currentNode] + cost[next-1])
            # degree가 0이면 큐에추가
            if(degree[next] == 0):
                queue.append(next)
    # 결과 출력
    print(result[W])