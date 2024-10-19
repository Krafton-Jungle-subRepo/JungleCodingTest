import sys
input = sys.stdin.readline

n = int(input())
drinks = [int(input()) for _ in range(n)]

if n < 3:
    print(sum(drinks))
else:
    dp = [drinks[0], drinks[0]+drinks[1], max(drinks[0]+drinks[1], drinks[0]+drinks[2], drinks[1]+drinks[2])] + [0] * (n-3)
    for i in range(3, n):
        dp[i]=max(drinks[i]+dp[i-2], drinks[i]+drinks[i-1]+dp[i-3], dp[i-1])
    print(max(dp))