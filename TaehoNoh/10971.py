import sys
input = sys.stdin.readline

n = int(input())

costs = [list(map(int, input().split())) for _ in range(n)]

min_cost = float('inf')

def dfs(cost, visited, cur_city, start_city):
    global min_cost
    
    if all(visited):
        if costs[cur_city][start_city] != 0 :
            min_cost = min(min_cost, cost + costs[cur_city][start_city])
        return
    
    for i in range(n):
        if not visited[i] and costs[cur_city][i] != 0 :
            visited[i] = True
            dfs(cost+costs[cur_city][i], visited, i, start_city)
            visited[i] = False
        

for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(0, visited, i, i)

print(min_cost)