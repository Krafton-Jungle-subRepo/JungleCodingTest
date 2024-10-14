import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))

dp = [1] * n

for i in range(1, len(boxes)):
    for j in range(i):
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[i], dp[j]+1) 
print(max(dp))