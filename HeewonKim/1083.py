# 소트
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())

def maximize_array():
    global S
    for i in range(N):
        max_idx = i
        for j in range(i + 1, min(N, i + S + 1)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        
        for j in range(max_idx, i, -1):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            S -= 1
            if S == 0: 
                return

maximize_array()
print(' '.join(map(str, arr)))
