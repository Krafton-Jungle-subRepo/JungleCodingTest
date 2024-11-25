T = 10

for t in range(1,T+1):
  dump = int(input())
  boxes = list(map(int,input().split()))

  print(boxes)

  for _ in range(dump):
    minIdx = boxes.index(min(boxes))
    maxIdx = boxes.index(max(boxes))

    boxes[minIdx] += 1
    boxes[maxIdx] -= 1
  
  result = max(boxes) - min(boxes)
  print(f"#{t} {result}")
