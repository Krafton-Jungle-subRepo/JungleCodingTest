from collections import deque
T = int(input())

def bfs(N,K):
  visited = set((N,0))
  q = deque([(N,0)])
  M = len(str(N))

  answer = 0
  while q:
    n, k = q.popleft()

    if k == K:
      answer = max(answer,n)
      continue
    
    n = list(str(n))
    for i in range(M-1):
      for j in range(i+1, M):
        
        if i == 0 and n[j] == '0':
          continue
        
        n[i],n[j] = n[j],n[i]
        nnum = int(''.join(n))
        if (nnum,k+1) not in visited:
          q.append((nnum,k+1))
          visited.add((nnum,k+1))
        n[i],n[j] = n[j],n[i]
  return answer if answer else -1

for t in range(1,T+1):
  N, K = map(int,input().split())
  print(f"#{t} {bfs(N,K)}")
