import sys
input = sys.stdin.readline

max_score = 0

n = int(input())

score = list(map(int,input().split()))

max_score = max(score)

for i in range(len(score)) :
    score[i] = score[i] / max_score * 100

total = sum(score)

answer = total / len(score)

print(answer)