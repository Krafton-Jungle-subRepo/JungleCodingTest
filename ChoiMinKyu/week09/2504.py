import sys
input = sys.stdin.readline

data = input().rstrip()
stack = []
answer = 0
tmp = 1

for i in range(len(data)):
  if data[i] == '(':
    tmp *= 2
    stack.append('(')
  
  if data[i] == '[':
    tmp *= 3
    stack.append('[')
  
  if data[i] == ')':
    if not stack or stack[-1] == '[':
      answer = 0
      break
    if data[i-1] == '(':
      answer += tmp
    tmp //=2
    stack.pop()
  
  if data[i] == ']':
    if not stack or stack[-1] == '(':
      answer = 0
      break
    if data[i-1] == '[':
      answer += tmp
    tmp //=3
    stack.pop()

if stack:
  print(0)
else:
  print(answer)

