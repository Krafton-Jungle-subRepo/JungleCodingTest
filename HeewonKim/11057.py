#오르막 수

import sys
N = int(sys.stdin.readline())

# 끝 번호가 0~9일때 10가지를 문자열의 길이 N+1 만큼 선언
dp = [([0] * 10) for _ in range(N+1)]

# 문자열의 길이 가 1일때는 0~9 모두 1이므로 dp[1][i] = 1
for i in range(10):
    dp[1][i] = 1

# 2부터 N까지, 끝 번호일때 계산
# i인 길이 문자열이고 끝번호가 j일때, 해당 가짓수는 i-1, 하나 작은 문자열에서 끝번호가 0~j일때의 합
# 문제 조건에 따라 10007 나머지 계산
for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])% 10007

# 길이가 N일 때의 합 
# 문제 조건에 따라 10007 나머지 계산
res = sum(dp[N]) % 10007

print(res)
