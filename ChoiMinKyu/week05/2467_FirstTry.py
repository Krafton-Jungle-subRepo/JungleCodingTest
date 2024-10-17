import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))

if N%2 != 0:
    idx1 = N//2 -1
    idx2 = N//2 +1

else:
    idx1 = N//2-1
    idx2 = N//2

tmp1 = 0
tmp2 = 0

mix = sys.maxsize

for i in range(N//2):
    currentMix = solutions[idx1] + solutions[idx2]
    if (currentMix < mix):
        tmp1 = solutions[idx1]
        tmp2 = solutions[idx2]
        mix = currentMix
        idx1 -= 1
        idx2 += 1

print(tmp1,tmp2)