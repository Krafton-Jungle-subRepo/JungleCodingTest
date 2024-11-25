import sys
input = sys.stdin.readline

T = 10
for t in range(1,T+1):
  N = int(input())
  buildings = list(map(int,input().split()))
  answer = 0
  for i in range(2,N-2):
    if buildings[i-2] < buildings[i] and buildings[i-1]<buildings[i] and buildings[i+1] < buildings[i] and buildings[i+2] < buildings[i]:
      answer += (buildings[i]-max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2]))
  print(f"#{t} {answer}")