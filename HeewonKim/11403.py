# 경로 찾기
import sys
N = int(sys.stdin.readline())
arcs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def floyd():
    for start in range(N):
        for i in range(N):
            for j in range(N):
                if(not arcs[i][j]):
                    arcs[i][j] = arcs[i][start] and arcs[start][j]

floyd()
for res in arcs:
    print(' '.join(map(str, res)))