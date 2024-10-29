# 텀 프로젝트
import sys
sys.setrecursionlimit(10**5)

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    visited = [False] * N
    in_cycle = [False] * N  
    res = N

    for i in range(N):
        if not visited[i]:  
            path = []
            while not visited[i]:
                visited[i] = True
                path.append(i)
                i = students[i] - 1

            if i in path:
                cycle_start = path.index(i)
                for j in path[cycle_start:]:
                    in_cycle[j] = True
                res -= len(path) - cycle_start

    print(res)
