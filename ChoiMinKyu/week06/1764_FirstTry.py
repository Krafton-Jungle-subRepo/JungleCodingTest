# 문제를 Array로 접근했기 때문에 시간초과가 날 수 밖에 없어 보인다. 
# -> 더 직접적으로 접근할 수 있는 방법은 없을까?
import sys
input = sys.stdin.readline

N,M =map(int,input().split())

notHear = []
answers = []
count = 0

for _ in range(N):
    notHear.append(input().rstrip())

for _ in range(M):
    name = input().rstrip()
    if name in notHear:
        answers.append(name)
        count += 1

print(count)
for ans in answers:
    print(ans)
