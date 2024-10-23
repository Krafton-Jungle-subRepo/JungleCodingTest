import sys, heapq
input = sys.stdin.readline

n = int(input())
nums = [0] + [int(input()) for _ in range(n)]
ans = []

cnt = n
is_ans = False

while True:
    if is_ans == True:
        print(cnt)
        for num in nums:
            if num != 0:
                ans.append(num)
                ans.sort()
        print(*ans, sep='\n')
        exit()
    is_ans = True
    for i in range(1, n+1):
        if nums[i] == 0:
            continue
        if i not in nums:
            nums[i] = 0
            cnt -= 1
            is_ans = False