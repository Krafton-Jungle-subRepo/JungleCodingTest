import sys
from collections import deque
input = sys.stdin.readline

def bfs(N,K):
  visited = set()
  queue = deque([(N,0)])
  visited.add((N,0))

  M = len(str(N))

  answer = 0
  while queue:
    n, k = queue.popleft()
    if k == K:
      answer = max(answer,n)
      continue
    n = list(str(n))

    for i in range(M-1):
      for j in range(i+1,M):
        if i == 0 and n[j] == '0':
          continue
        n[i],n[j] = n[j],n[i]
        nnum = int(''.join(n))
        if (nnum,k+1) not in visited:
          queue.append((nnum,k+1))
          visited.add((nnum,k+1))
        n[i],n[j] = n[j],n[i]
  return answer if answer else -1


N, K = map(int,input().split())
print(bfs(N,K))