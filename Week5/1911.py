from math import ceil
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
ans = 0
cur = 0

water = [list(map(int, input().split())) for _ in range(N)]
water.sort()

while water:
    start, end = water.pop(0)
    if cur > end:
        continue
    if cur < start:
        cur = start
    
    temp = ceil((end - cur) / L)
    ans += temp
    cur += temp * L
    
print(ans)