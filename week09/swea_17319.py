import sys
input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
  N = int(input())
  sentence = input().rstrip()

  if ( N % 2 == 0):
    front = sentence[:N//2]
    back = sentence[N//2:]
    if front == back:
      print(f"#{t} Yes")
      continue

  print(f"#{t} No")