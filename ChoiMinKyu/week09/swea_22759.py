T = int(input())

for _ in range(T):
    L, R = map(int, input().split())
    
    # Check if X = R + 1 works
    if (R + 1) % L >= (R + 1) // 2:
        print("yes")
    else:
        print("no")
