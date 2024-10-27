# 팰린드롬?
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [([0] * N) for _ in range(N)]

def CheckSame(startIdx, endIdx):
    if(arr[startIdx] != arr[endIdx]):
        return 0
    if(startIdx + 1 == endIdx):
        return 1
    return dp[startIdx+1][endIdx-1]

for i in range(N):
    startIdx = 0
    endIdx = i
    while(endIdx < N):
        if(i == 0):
            dp[startIdx][endIdx] = 1
        else:
            dp[startIdx][endIdx] = CheckSame(startIdx, endIdx)
        startIdx+=1
        endIdx+=1


M = int(sys.stdin.readline())
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp[S-1][E-1])