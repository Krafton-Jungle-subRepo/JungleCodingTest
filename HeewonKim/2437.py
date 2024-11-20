# 저울
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

total = 0
for i in range(N):
    if(total + 1 < arr[i]):
        break
    total += arr[i]

print(total + 1)
