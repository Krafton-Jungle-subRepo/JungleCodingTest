import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
A.sort()

count = 0
for k in range(N):
  is_good = False
  for i in range(k):
    for j in range(k):
      if (i != j):
        if is_good == True:
          break
        tmp = A[i] + A[j]
        if tmp == A[k]:
          count += 1
          is_good = True
          break

print(count)