# 그냥 오름차순 정렬하고 더하면 되는 문제였는데 너무 어렵게 생각함
import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))
P.sort()

answer = 0

for i in range(N):
    for j in range(0,i+1):
        answer += P[j]

print(answer)