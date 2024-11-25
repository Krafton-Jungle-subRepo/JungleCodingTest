# 빠른 입력을 위해 sys.stdin 사용
import sys
input = sys.stdin.readline
# maxsize를 INF로 선언해 사용
INF = sys.maxsize

def bellmanFord(start):
    # 시작점->시작점 거리를 0으로 설정 후 Bellman-Ford 이용
    distance[start] = 0
    # N-1번 반복
    for _ in range(N - 1):
        for curr, next, cost in bus:
            if distance[curr] != INF and distance[next] > distance[curr] + cost:
                distance[next] = distance[curr] + cost

    # N번째 반복에서 음수 사이클 확인
    for curr, next, cost in bus:
        if distance[curr] != INF and distance[next] > distance[curr] + cost:
            return False  # 음수 사이클 존재 시 False 반환
    # 음수 사이클이 없으면 True 반환
    return True

N,M = map(int,input().split())
bus = list(tuple(map(int,input().split())) for _ in range(M))
distance = [INF] * (N+1)
# 시작점 1로부터 다른 점까지의 거리를 bellmanFord로 계산
# 음수 사이클이 없다면 다른 점까지의 거리 출력
if bellmanFord(1):
  for i in range(2,len(distance)):
    if distance[i] >= INF:
      print(-1)
    else:
      print(distance[i])
# 음수 사이클이 있으면 -1 출력
else:
  print(-1)