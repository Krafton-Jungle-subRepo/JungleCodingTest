import sys
input = sys.stdin.readline

N = int(input())
voca = list(input().rstrip() for _ in range(N))
result = []
cnt = 0

for v1 in range(N-1):
  for v2 in range(v1+1,N):
    tmp = 0
    length = min(len(voca[v1]),len(voca[v2]))
    for i in range(length):
      if voca[v1][i] == voca[v2][i]:
        tmp += 1
      else:
        break
    if tmp > cnt:
      result = [voca[v1],voca[v2]]
      cnt = tmp

if result:
  print (result[0])
  print (result[1])
else:
  print(0)