import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
# 입력 parsing하기
for i in range(1,n+1):
  cost, indegree, *lst = map(int,input().split())
  dp[i] = cost
  for x in lst:
    graph[i].append(x)
# dp로 해결
for i in range(1,n+1):
  tmp = 0
  for j in graph[i]:
    tmp = max(tmp,dp[j])
  dp[i] += tmp

print(max(dp))