# 다각형의 면적
import sys

N = int(sys.stdin.readline())
dot = [(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
dot.append(dot[0])
res = 0

# 다각형의 면적 구하는 신발끈 공식
# abs(0.5 * ∑(xi*y(i+1)−yi*x(i+1)))
for i in range(N):
    res += dot[i][0]*dot[i+1][1] - dot[i][1]*dot[i+1][0]
print(abs(res*0.5))