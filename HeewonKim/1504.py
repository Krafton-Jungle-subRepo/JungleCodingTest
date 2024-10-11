# 특정한 최단 경로
import sys
import heapq

# 무한대를 sys.maxsize로 설정
INF = sys.maxsize

# 입력
N, E = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().split())
    edges[start].append([end, cost])
    edges[end].append([start, cost])

V1, V2 = map(int, sys.stdin.readline().split())


# start에서 end로 이동하는 최단경로
def Dijkstra(start, end):
    # 최단거리 갱신 배열, 힙 선언
    cost = [sys.maxsize] * (N+1)
    cost[start] = 0
    heap = []
    # 힙에 출발지점 push
    heapq.heappush(heap, [0, start])

    # 힙이 빌때까지
    while(heap):
        currentCost, currentNode = heapq.heappop(heap)
        # 힙에서 pop한 노드 순회
        for j in range(len(edges[currentNode])):
            nextNode, nextCost = edges[currentNode][j]
            # 다음 노드의 비용보다 힙에 저장된 비요이 더 크면 skip
            if(currentCost >= cost[nextNode]):
                continue

            else:
                # 만약 저장된 다음 노드의 비용보다 현재 노드+다음노드 거리가 더 비용이 낮다면 갱신, 힙에 push
                if(cost[nextNode] > cost[currentNode] + nextCost):
                    cost[nextNode] = cost[currentNode] + nextCost
                    heapq.heappush(heap, [cost[nextNode], nextNode])
    
    return cost[end]

# 시작점, 도착지
start = 1
end = N

# 세 가지 경로의 비용을 각각 계산
route1 = Dijkstra(start, V1) + Dijkstra(V1, V2) + Dijkstra(V2, end)
route2 = Dijkstra(start, V2) + Dijkstra(V2, V1) + Dijkstra(V1, end)

# 경로가 없을 경우(INF인 경우)를 처리
result = min(route1, route2)
if(result >= INF):
    print(-1)
else:
    print(result)
