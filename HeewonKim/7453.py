# 합이 0인 네 정수
import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = [[] for _ in range(4)]

for _ in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    for i in range(4):
        arr[i].append(num[i])

sumAB = []
sumCD = []

for i in range(N):
    for j in range(N):
        sumAB.append(arr[0][i] + arr[1][j])
        sumCD.append(arr[2][i] + arr[3][j])

countCD = Counter(sumCD)

count = 0
for total in sumAB:
    count += countCD[-total]

print(count)
