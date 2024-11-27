import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellman_ford(start):
  distance[start] = 0
  for i in range(N):
    for A, B, C in roads:
      if distance[A] != INF and distance[A]+C < distance[B]:
        distance[B] = distance[A]+C

N,M = map(int,input().split())
roads = []
for _ in range(M):
  A, B, C = map(int, input().split())
  # 양방향으로 추가
  roads.append((A,B,C))
  roads.append((B,A,C))
roads.sort()
distance = [INF]*(N+1)

bellman_ford(1)

print(distance[N])