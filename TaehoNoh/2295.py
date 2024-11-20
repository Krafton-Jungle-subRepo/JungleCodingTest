import sys
input = sys.stdin.readline

n = int(input())

nums = set()

for _ in range(n):
    nums.add(int(input()))

sums = set()

for i in nums:
    for j in nums:
        sums.add(i+j)

ans = []

for i in nums:
    for j in nums:
        if (i - j) in sums:
            ans.append(i)

print(max(ans))