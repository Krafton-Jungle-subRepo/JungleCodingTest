import sys
input = sys.stdin.readline
MAXSIZE = sys.maxsize

N = int(input())
users = [[MAXSIZE]*(N+1) for _ in range((N+1))]

a = b = 0
while (a != -1 and b != -1):
    a, b = map(int,input().split())
    if (a != -1 and b != -1):
        users[a][b] = users[b][a] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            users[i][j] = min(users[i][j], users[i][k]+users[k][j])
        users[i][i] = 1

answers = [0] * (N+1)

for i in range(1,N+1):
    answers[i] = max(users[i][1:N+1])

answers = answers[1:]
score = min(answers)
count = 0

for ans in answers:
    if ans == score:
        count+= 1

print(score, count)

for i in range(len(answers)):
    if answers[i] == score:
        print(i+1,end=' ')
