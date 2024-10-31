# 웜홀
import sys
input = sys.stdin.readline
INF = float('inf')

def bellman_ford(N, edges):
    dist = [0] * (N + 1)  # 모든 노드의 초기 거리를 0으로 설정

    for i in range(N):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == N - 1:
                    return True  # 음의 사이클 존재
    return False  # 음의 사이클 없음

T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))
    if bellman_ford(N, edges):
        print("YES")
    else:
        print("NO")
