from collections import deque

def bfs(choices):
  answer = 0
  visited = set()
  q = deque(choices[0])
  visited.add(0)

  while q:
    rec, cal = q.popleft()


T = int(input())

for t in range(1,T+1):
  N, L = map(int,input().split())

  choices = list(tuple(map(int,input().split())) for _ in range(N))

