import sys
input = sys.stdin.readline

data = input().rstrip()
stack = []

result = 0
tmp = 1

for i in range(len(data)):
    if data[i] == '(':
        stack.append(data[i])
        tmp *= 2
    if data[i] == '[':
        stack.append(data[i])
        tmp *= 3
    if data[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if data[i-1] == '(':
            result += tmp
        tmp //= 2
        stack.pop()
    if data[i] == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break
        if data[i-1] == '[':
            result += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)