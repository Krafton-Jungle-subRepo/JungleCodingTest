import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

if n == 2:
    print(2**m * (cards[0] + cards[1]))
    exit()

for i in range(m):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    for _ in range(2):
        heapq.heappush(cards, a + b)

print(sum(cards))