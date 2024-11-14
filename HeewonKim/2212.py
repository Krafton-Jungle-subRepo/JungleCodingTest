# 센서
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
if K >= N:
    print(0)  
else:
    sensors = list(map(int, sys.stdin.readline().split()))
    sensors.sort()

    distances = []
    for i in range(1, N):
        distances.append(sensors[i] - sensors[i-1])

    distances.sort(reverse=True)  

    for _ in range(K-1):
        distances.pop(0)  

    print(sum(distances)) 
