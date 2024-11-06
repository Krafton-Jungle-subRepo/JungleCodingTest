# 좋다
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

res = 0

for i in range(N):
    target = arr[i]
    left, right = 0, N - 1

    while left < right:
        if left == i:  
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        two_sum = arr[left] + arr[right]
        
        if two_sum == target:
            res += 1
            break
        elif two_sum < target:
            left += 1
        else:
            right -= 1

print(res)
