import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*8)

n = int(input())

dp = [0] * 1000001

for i in range(2, n+1):
    # 2와 3으로 나누어 떨어지지 않으면 무조건 -1
    dp[i] = dp[i-1]+1

    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])