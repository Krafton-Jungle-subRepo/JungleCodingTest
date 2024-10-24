import sys
input = sys.stdin.readline

rectangle = [list(map(int, input().split())) for _ in range(4)]
max_val = 0
ans = 0

for r in rectangle:
    max_val = max(max(r), max_val)

graph = [[0] * max_val for _ in range(max_val)]

while rectangle:
    x1, y1, x2, y2 = rectangle.pop(0)
    for y in range(y1, y2):
        for x in range(x1, x2):
            if graph[y][x] == 1:
                continue
            else:
                graph[y][x] = 1

for g in graph:
    ans += sum(g)
print(ans)