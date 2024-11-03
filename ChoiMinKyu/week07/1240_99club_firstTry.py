import sys
input = sys.stdin.readline

def sol(start,end):
    global N
    global graph
    global visited

    answer = 0
    stack = [start]
    visited[start] = 1

    while stack:
        v = stack.pop()

        for i in range(1,N+1):
            if graph[v][i] > 0 and visited[i] == 0:
                answer += graph[v][i]
                if end == i:
                    return answer
                stack.append(i)
                visited[i] = 1
    

N, M = map(int,input().split())
graph = [[0]*(N+1) for _ in range((N+1))]

for _ in range(N-1):
    a, b, cost = map(int,input().split())
    graph[a][b] = graph[b][a] = cost

for _ in range(M):
    visited = [0]*(N+1)
    a, b =map(int,input().split())
    result = sol(a,b)
    print(result)