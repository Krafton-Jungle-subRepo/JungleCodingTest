import sys
input = sys.stdin.readline

def fibo(x):
    if dp[x] != 0 or x < 3:
        return dp[x]
    else:
        return fibo(x-1) + fibo(x-2)

n = int(input())
vips = [int(input()) for _ in range(int(input()))]
dp = [1, 1, 2] + [0] * (n-2)
divide = []
ans = []
cnt = 0

if len(vips) == n:
    print(1)
    exit()

for i in range(1, n+2):
    cnt += 1
    if i in vips or i == n+1:
        if cnt != 1:
            divide.append(cnt-1)
        cnt = 0

ans = fibo(divide.pop(0))
for d in divide:
    ans *= fibo(d)
print(ans)