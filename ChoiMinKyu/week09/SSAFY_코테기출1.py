import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N, K = map(int,input().split())
  sequence = list(map(int,input().split()))
  sequence.sort()
  result = []
  idx = 0

  for s1 in sequence:
    if idx >= K:
        break
    for s2 in sequence:
      if idx >= K:
        break
      result.append((s1,s2))
      idx += 1
  
  result.sort(key=lambda x:(x[0],x[1]))

  print(result[idx-1][0]+result[idx-1][1])