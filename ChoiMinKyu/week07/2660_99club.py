# 빠른 입력을 위해 sys.stdin 사용
import sys
input = sys.stdin.readline
# 시스템 내 maxsize 사용
MAXSIZE = sys.maxsize

# 회원 수 입력, 회원들 인접 행렬 그래프로 표현
N = int(input())
users = [[MAXSIZE]*(N+1) for _ in range((N+1))]

# 친구 관계 입력
a = b = 0
while (a != -1 and b != -1):
    a, b = map(int,input().split())
    if (a != -1 and b != -1):
        users[a][b] = users[b][a] = 1
# Floyd-warshall 알고리즘 이용
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            users[i][j] = min(users[i][j], users[i][k]+users[k][j])
        # 이 때, users[i][i] = 1로 고정
        users[i][i] = 1
# 각 회원에 대해 점수를 할당할 배열
answers = [0] * (N+1)
# 배열에 점수 할당
for i in range(1,N+1):
    answers[i] = max(users[i][1:N+1])
# 인덱스 0번은 사용하지 않을 것이므로 삭제
answers = answers[1:]
# 회장 후보의 점수
score = min(answers)
# 회장 후보의 수
count = 0
for ans in answers:
    if ans == score:
        count+= 1
# 회장 후보의 점수, 회장 후보의 수 출력
print(score, count)
# 회장 후보 출력
for i in range(len(answers)):
    if answers[i] == score:
        print(i+1,end=' ')
