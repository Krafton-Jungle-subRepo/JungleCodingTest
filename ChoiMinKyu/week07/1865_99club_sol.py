# 입력을 빠르게 받기 위해 sys.stdin 사용
import sys
input = sys.stdin.readline
# 최댓값으로 sys.maxsize 사용
INF = sys.maxsize

# bellmanFord에서 모든 출발지에 대해 음수 사이클 존재 확인
def bellmanFord():
    for i in range(N):
        for j in range(len(edges)):
            curr, next, cost = edges[j]
            if distance[next]>distance[curr]+cost:
                distance[next] = distance[curr] + cost
                # 음수 사이클이 존재하면 True 반환
                if i == N-1:
                    return True
    # 음수 사이클 없으면 False 반환
    return False
# 테스트 케이스 입력
TC = int(input())
# 테스트 케이스만큼 반복
for _ in range(TC):
    # 지점 개수, 도로 개수, 웜홀 개수
    N, M, W = map(int,input().split())
    # 지점으로부터의 거리
    distance = [INF]*(N+1)
    # 각 간선을 할당할 배열
    edges = []

    # 도로 입력
    for _ in range(M):
        S, E, T = map(int,input().split())
        # 도로는 양방향 입력
        edges.append((S,E,T))
        edges.append((E,S,T))
    # 웜홀 입력
    for _ in range(W):
        S, E, T = map(int,input().split())
        # 웜홀은 단방향 입력 (음의 가중치를 가진 도로로 판단)
        edges.append((S,E,(-T)))
    # bellmanFord 호출, 결과 출력
    if bellmanFord():
        print("YES")
    else:
        print("NO")