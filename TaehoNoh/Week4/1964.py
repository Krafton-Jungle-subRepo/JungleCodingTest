import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    scores = []

    for _ in range(n):
        a, b = list(map(int,input().split()))
        scores.append((a,b))

    scores.sort()
    count = 1

    max = scores[0][1]
    for i in range(1, n):
        if max > scores[i][1]:
            count+=1
            max= scores[i][1]

    print(count)
