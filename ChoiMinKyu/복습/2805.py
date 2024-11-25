def cutting_tree(height):
  save = 0
  for i in range(len(trees)):
    if trees[i] > height:
      save += trees[i]-height
      # trees[i] - save
  return save


N,M = map(int,input().split())
trees = list(map(int,input().split()))
height = max(trees)-1
save = 0

while True:
  save = cutting_tree(height)
  if save >= M:
    break
  else:
    height -= 1

print(height)