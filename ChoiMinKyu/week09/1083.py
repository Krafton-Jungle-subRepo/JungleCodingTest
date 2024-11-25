N = int(input())
arr = list(map(int,input().split()))
S = int(input())

for i in range(N):
  if S <= 0:
    break

  max_val = max(arr[i:i+S+1])
  max_idx = arr.index(max_val)

  while i != max_idx:
    if S <= 0:
      break
    arr[max_idx],arr[max_idx-1] = arr[max_idx-1],arr[max_idx]
    max_idx -= 1
    S -= 1

for x in arr:
  print(x,end=" ")