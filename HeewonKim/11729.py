# 하노이 탑 이동 순서
import sys

N = int(sys.stdin.readline())
res = []

def hanoi(n, start, via, end):
    if(n == 0):
        return 0
    
    total = 0
    total += hanoi(n-1, start, end, via)
    total += 1
    res.append([start, end])
    total += hanoi(n-1, via, start, end)

    return total

print(hanoi(N, 1, 2, 3))
for start, end in res:
    print(start, end)