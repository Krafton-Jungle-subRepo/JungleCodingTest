import sys
input = sys.stdin.readline

score = list(list(map(int,input().split())) for _ in range(5))

idx = 0
best = 0
for i in range(5):
    current = sum(score[i])
    if best < current:
        idx = i
        best = current

print(idx+1,best)