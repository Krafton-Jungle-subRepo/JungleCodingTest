import sys
input = sys.stdin.readline

n, target = map(int, input().split())

trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end :
    mid = (start + end) // 2

    total = 0 # 잘린 나무의 길이 총합
    for i in trees:
        if i >= mid :
            total += i - mid

    if total >= target :
        start = mid + 1
    else :
        end = mid - 1

print(end)