N = int(input())

arr = list(map(int,input().split()))
aLen = len(arr)
S = int(input())
tmp = 0
check_limit = False

for i in range(1,aLen):
  if check_limit:
    break
  if arr[i-1] < arr[i]:
    arr[i-1],arr[i] = arr[i],arr[i-1]
    tmp += 1
    if tmp >= S:
      check_limit = True

for x in arr:
  print(x,end=" ")