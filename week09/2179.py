import sys
input = sys.stdin.readline

N = int(input())
voca = list(input().rstrip() for _ in range(N))
result = {}

for v1 in voca:
  for v2 in voca:
    # 두 단어가 서로 다를 때
    if v1 != v2:
      tmp = 0
      # 더 짧은 문자열 길이만큼 반복
      l = min(len(v1),len(v2))
      for i in range(l):
        # 맨 앞 문자부터 문자가 같을 때 tmp+1
        if v1[i] == v2[i]:
          tmp += 1
        # 문자가 다르면 break
        else:
          break
      if tmp > 0 and result.get((v1,v2)) == None and result.get((v2,v1)) == None:
        result[(v1,v2)] = tmp

answer = max(result,key=result.get)
print(answer[0])
print(answer[1])