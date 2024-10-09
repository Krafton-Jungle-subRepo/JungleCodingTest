import sys
from collections import deque

input = sys.stdin.readline
n, w, l = map(int, input().split())  # 트럭 수, 다리 길이, 최대 하중
trucks = deque(map(int, input().split()))
bridge = deque([0] * w) 
total_weight = 0
time = 0

while trucks or total_weight > 0:
    time += 1
    total_weight -= bridge.popleft()

    if trucks:
        if total_weight + trucks[0] <= l:
            truck = trucks.popleft()
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)

print(time)