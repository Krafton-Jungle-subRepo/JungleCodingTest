import sys
input = sys.stdin.readline
import heapq

N = int(input())
left = []
right = []
result = []

for _ in range(N):
  x = int(input())

  heapq.heappush(left,-x)
  heapq.heappush(right,x)

  if -left[0] > right[0]:
    left_max = -heapq.heappop(left)
    right_min = heapq.heappop(right)
    heapq.heappush(left,-right_min)
    heapq.heappush(right,left_max)
  
  result.append(-left[0])

for res in result:
  print(res)