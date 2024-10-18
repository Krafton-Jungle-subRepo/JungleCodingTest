import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
prices = list(map(int, input().split()))
sales = [[] for _ in range(n)]
min_ans = float('inf')

for i in range(n):
    for _ in range(int(input())):
        num, sale = map(int, input().split())  
        sales[i].append((num-1, sale))

orders = list(map(list, permutations(range(n), n)))

for order in orders:
    temp_sale = [0] * n
    total = 0
    for o in order:
        if total > min_ans:
            break
        total += prices[o] - temp_sale[o]
        if len(sales[o]) == 0:
            continue
        else:
            for sale in sales[o]:
                num, discount = sale
                if temp_sale[num] + discount >= prices[num]:
                    temp_sale[num] = prices[num] - 1
                else:
                    temp_sale[num] += discount
    min_ans = min(min_ans, total)

print(min_ans)