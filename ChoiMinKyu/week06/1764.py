import sys
input = sys.stdin.readline

dict = {}
answers = []

N, M = map(int,input().split())

for _ in range(N):
    name = input().rstrip()
    dict[name] = 1

for _ in range(M):
    name = input().rstrip()
    if name in dict:
        answers.append(name)

print(len(answers))
for ans in answers:
    print(ans)