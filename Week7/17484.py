import sys

n, m = map(int, input().split())
rockets = [list(map(int, input().split())) for _ in range(n)]
dir = {1: (1, -1), 2: (1, 0), 3: (1, 1)}

def dfs(i, j, cur_dir, ans, cost):
    if i == n-1:
        return min(ans, cost)
    for k in range(1, 4):
        if cur_dir != k:
            if 0 <= i+dir[k][0] < n and 0 <= j+dir[k][1] < m:
                ans = dfs(i+dir[k][0], j+dir[k][1], k, ans, cost+rockets[i+dir[k][0]][j+dir[k][1]])
    return ans

ans = int(sys.maxsize)
for i in range(m):
    ans = min(dfs(0, i, 0, ans, rockets[0][i]), ans)

print(ans)