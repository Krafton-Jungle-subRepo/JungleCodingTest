import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
dist = []

if n <= k:
    print(0)
    exit()

sensors.sort()

for i in range(1, n):
    dist.append(sensors[i] - sensors[i-1])
for _ in range(k-1):
    dist.pop(dist.index(max(dist)))

print(sum(dist))