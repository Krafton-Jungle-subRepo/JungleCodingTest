import sys
input = sys.stdin.readline
INF = sys.maxsize

def dfs(N, currentx,currenty):
    if currentx == N-1 and currenty == N-1:
        return graph[N-1][N-1]
    

    for i in range(4):
        nextx = currentx+dx[i]
        nexty = currenty+dy[i]

        nextvalue = []
        if 0<=nextx<N and 0<=nexty<N:
            nextvalue.append(dfs(N,nextx,nexty))

    return graph[currentx][currenty] + min(nextvalue)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = -1
while (1):
    N = int(input())
    if N == 0:
        break
    graph = []
    for i in range(N):
        graph.append(list(map(int,input().split())))
    
    result = dfs(N,0,0)
    print(result)
    

