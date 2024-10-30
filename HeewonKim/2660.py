# 회장 뽑기
import sys

N = int(sys.stdin.readline())
edges = [([sys.maxsize]*(N+1)) for _ in range (N+1)]

for i in range(1, N+1):
    edges[i][i] = 0
while(1):
    num1, num2 = map(int, sys.stdin.readline().split())
    if(num1 == -1 and num2 == -1):
        break
    edges[num1][num2] = 1
    edges[num2][num1] = 1

def floyd():
    for via in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if(i!=j  and via!= i and j!= via):
                    edges[i][j] = min(edges[i][via] + edges[via][j], edges[i][j])
floyd()

res = [0] * (N+1)
for i in range(1, N+1):
    res[i] = max(edges[i][1:])

score = min(res[1:])
num = 0
resarr = []
for i in range(1, N+1):
    if(res[i] == score):
        resarr.append(i)
        num += 1
print(score, num)
print(' '.join(map(str, resarr)))