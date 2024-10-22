import sys, heapq
input = sys.stdin.readline

rooms = []
n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort()

heapq.heappush(rooms, (lectures[0][1]))
for i in range(1, len(lectures)):
    if len(rooms) == 0:
        heapq.heappush(rooms, (lectures[i][1]))
    else:
        if rooms[0] <= lectures[i][0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, lectures[i][1]) 
print(len(rooms))