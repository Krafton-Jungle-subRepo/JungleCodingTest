import sys

N, M = map(int, sys.stdin.readline().split())
app = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

costRange = sum(cost)
dp = [0] * (costRange + 1)

for i in range(N):
    for j in range(costRange, cost[i]-1, -1):
        dp[j] = max(dp[j], dp[j-cost[i]] + app[i])

for i in range(costRange+1):
    if(dp[i] >= M):
        print(i)
        break
