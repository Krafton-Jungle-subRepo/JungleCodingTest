# 도서관
import sys

N, M = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))

positive = []
negative = []

for book in books:
    if book > 0:
        positive.append(book)
    else:
        negative.append(-book)

positive.sort(reverse=True)
negative.sort(reverse=True)

res = 0

for i in range(0, len(positive), M):
    res += positive[i] * 2 

for i in range(0, len(negative), M):
    res += negative[i] * 2 

if positive and negative:
    res -= max(positive[0], negative[0])
elif positive:
    res -= positive[0]
elif negative:
    res -= negative[0]

print(res)
