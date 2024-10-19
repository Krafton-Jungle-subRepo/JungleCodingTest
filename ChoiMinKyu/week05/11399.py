import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))
tmp = P.copy()

center = 0
left = 0
right = N-1

if N%2 != 0:
    center = min(P)
    del P[P.index(min(P))]


while left < right:

    tmp[left] = min(P)
    del P[P.index(min(P))]
    tmp[right] = min(P)
    del P[P.index(min(P))]
    left += 1
    right -= 1

if N%2 != 0:
    tmp[N//2+1] = center

print(tmp)

answer = 0
current = tmp[0]
for n in tmp:
    answer += current
    current = answer

print(answer)
