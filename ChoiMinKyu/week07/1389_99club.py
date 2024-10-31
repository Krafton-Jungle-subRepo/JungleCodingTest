# 빠른 입력을 위해 sys.stdin 사용
import sys
input = sys.stdin.readline
# MAXSIZE 구현 위해 시스템 maxsize 사용
MAX = sys.maxsize

# 유저의 수 N, 관계의 수 M 입력
N, M = map(int,input().split())
# 유저 관계를 그래프 (인접 행렬)로 구현
users = [[MAX]*(N+1) for _ in range(N+1)]
# 케빈 베이컨의 수를 할당할 배열
kevin = [0]*(N+1)

# 친구 관계 입력
for _ in range(M):
    A, B = map(int,input().split())
    users[A][B] = users[B][A] = 1

# Floyd-Warshall 이용
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            users[i][j] = min(users[i][j], users[i][k] + users[k][j])

# 케빈 베이컨의 수 입력
for i in range(1,N+1):
    for j in range(1,N+1):
        if users[i][j] != MAX:
            kevin[i] += users[i][j]
# 0번 인덱스는 사용하지 않을 것이므로, maxsize로 수정
kevin[0] = MAX
# 결과 출력
print(kevin.index(min(kevin)))