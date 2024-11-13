import sys
input = sys.stdin.readline

N = int(input())
voca = list(input().rstrip() for _ in range(N))
voca.sort()
result = {}

for i in range(N-1):
  if voca[i][0] == voca[i+1][0]:
    tmp = 0
    length = min(len(voca[i]),len(voca[i+1]))
    for j in range(length):
      if voca[i][j] == voca[i+1][j]:
        tmp += 1
      else:
        break
    if result.get((voca[i],voca[i+1])) == None and result.get((voca[i+1],voca[i])) == None:
      result[(voca[i],voca[i+1])] = tmp

answer = max(result,key=result.get)
print(answer[0])
print(answer[1])