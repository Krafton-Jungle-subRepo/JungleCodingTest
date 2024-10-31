import sys
input = sys.stdin.readline

def solution(t, p):
    answer = 0
    for i in range(len(t)):
        if (len(t) - i >= len(p)):
            tmp = t[i:i+len(p)]
            if (int(tmp) <= int(p)):
                answer+=1
    return answer

t = input()
p = input()
print(solution(t,p))