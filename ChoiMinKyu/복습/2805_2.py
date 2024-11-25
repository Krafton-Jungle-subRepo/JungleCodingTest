N, M = map(int,input().split())
trees = list(map(int,input().split()))

low = 0
high = max(trees)
result = 0

while low <= high:
  save = 0
  pivot = (low+high)//2

  for tree in trees:
    if pivot < tree:
      save += (tree-pivot)
  
  if save >= M:
    result = pivot
    low = pivot + 1
    
  else:
    high = pivot -1

print(result)