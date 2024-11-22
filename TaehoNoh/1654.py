import sys
input = sys.stdin.readline

K, N = map(int,input().split())
a = [int(input()) for _ in range(K)]
st, en = 1, max(a)

while st <= en :
    mid = (st + en) // 2

    lines = 0

    for i in a :
        lines += i // mid 
    
    if lines >= N :
        st = mid + 1
    else :
        en = mid - 1

print(en)