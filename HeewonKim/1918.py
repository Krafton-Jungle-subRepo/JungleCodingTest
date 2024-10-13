# 후위 표기식
import sys

inputStr = list(sys.stdin.readline().rstrip('\n'))
stack = []
# 연산자 우선 순위
operator = {'+' : 1, '-': 1, '*':2, '/':2, '(':3, ')':3}

# 문자열 전체 순회
for i in range(len(inputStr)):
    # 만약 연산자가 아니면 출력후 스킵
    if(inputStr[i] not in operator):
        print(inputStr[i], end='')
        continue

    # 여는 괄호일 경우 스택에 넣고 스킵
    if(inputStr[i] == '('):
        stack.append(inputStr[i])
        continue

    # 스택이 비어있는 경우 삽입
    if(len(stack) == 0):
        stack.append(inputStr[i])
    
    # 스택이 비어있지 않은 경우
    else:
        # 닫는 괄호가 아니면
        if(inputStr[i] != ')'):
            # 현재 연산자의 우선 순위가 스택 가장위의 연산자 우선순위보다 크면 스택에 삽입
            if(operator[inputStr[i]] > operator[stack[len(stack)-1]]):
                stack.append(inputStr[i])
            # 스택 위의 연산자의 우선순위가 현재 연산자 우선 순위보다 같거나 크다면
            else:
                # 스택이 비거나, 여는 괄호가 나오거나, 우선순위가 낮아질때까지 반복
                while(len(stack) != 0 and operator[inputStr[i]] <= operator[stack[len(stack)-1]] and stack[len(stack)-1] != '('):
                    print(stack.pop(), end='')
                # 스택에 현재 연산자 삽입
                stack.append(inputStr[i])
        
        # 닫는 괄호라면
        else:
            # 여는 괄호가 나올때까지 연산자 출력
            while(len(stack) != 0):
                    current = stack.pop()
                    if(current == '('):
                        break
                    print(current, end='')

# 스택이 빌때까지 출력
while(len(stack) != 0):
    print(stack.pop(), end='')
