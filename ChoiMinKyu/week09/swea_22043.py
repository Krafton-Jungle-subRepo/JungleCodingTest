T = int(input())

for _ in range(T):
  N = int(input())
  a = [float(input()) for _ in range(N)]

  answer = 0
  for i in range(N-1):
    for j in range(i+1,N):
      tmp= a[i]*a[j]
      if int(tmp) == tmp:
        answer += 1
  print(answer)