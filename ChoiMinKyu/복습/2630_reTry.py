def sol(x,y,n):
  global white
  global blue

  color = papers[x][y]
  same_color = True

  for i in range(x,x+n):
    for j in range(y,y+n):
      if papers[i][j] != color:
        same_color = False
        break
    
    if not same_color:
      break

  if same_color:
    if color == 1:
      blue += 1
    else:
      white += 1
  
  else:
    half = n//2
    sol(x,y,half)
    sol(x,y+half,half)
    sol(x+half,y,half)
    sol(x+half,y+half,half)

N = int(input())
papers = list(list(map(int,input().split())) for _ in range(N))
blue = 0
white = 0
sol(0,0,N)

print(white)
print(blue)