import sys
input = sys.stdin.readline

data = input().rstrip()
stack = []
stick = 0
count = 0

# 입력받은 괄호만큼 돌면서
for i in range(len(data)):
    # 여는 괄호일 때, 스택에 추가
    if data[i] == '(':
        stack.append(data[i])
    # 닫는 괄호일 때
    else:
        # 이전 괄호가 여는 괄호일 때 == 레이저 쐈을 때
        if data[i-1] == '(':
            # 스택에서 pop하고 스택 크기만큼 카운트
            stack.pop()
            count += len(stack)
        # 이전 괄호가 닫는 괄호였을 때
        else:
            # 스택에서 pop 하고 카운트 1 증가
            stack.pop()
            count += 1

print(count)