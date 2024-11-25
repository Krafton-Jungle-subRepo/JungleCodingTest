import sys
input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
  S = list(input().rstrip())
  N = len(S)
  tmp = S.copy()
  tmp = tmp[::-1]

  if S != tmp:
    print(f"#{t} NO")
    continue
  
  left = S[:(N-1)//2]
  tmp = left[::-1]

  if left != tmp:
    print(f"#{t} NO")
    continue

  right = S[(N-1)//2+1:]
  tmp = right[::-1]

  if right != tmp:
    print(f"#{t} NO")
    continue

  print(f"#{t} YES")
