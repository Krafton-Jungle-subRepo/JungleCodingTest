import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(input().rstrip())

answer = []
cnt = K

for num in nums:
    while answer and cnt > 0 and answer[-1] < num:
        answer.pop()
        cnt -= 1
    answer.append(num)

print(''.join(answer[:N-K]))