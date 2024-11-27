import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    # 우선순위 큐 사용
    pq = []
    heapq.heappush(pq, (0, start))  # (거리, 헛간 번호)
    distance[start] = 0

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        # 이미 처리된 노드라면 무시
        if curr_dist > distance[curr_node]:
            continue

        for next_node, cost in graph[curr_node]:
            new_dist = curr_dist + cost
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

# 입력 처리
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

# 거리 배열 초기화
distance = [INF] * (N + 1)

# 다익스트라 실행
dijkstra(1)

# 결과 출력
print(distance[N])