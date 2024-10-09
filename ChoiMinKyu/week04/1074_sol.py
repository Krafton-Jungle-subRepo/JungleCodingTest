import sys
sys.setrecursionlimit(10**6)

def zTraversal(n, startX, startY, r, c, value):
    if n == 1:
        # 기저 사례: 2x2 배열에서 위치를 찾아 값을 반환
        if startX == r and startY == c:
            return value
        if startX == r and startY + 1 == c:
            return value + 1
        if startX + 1 == r and startY == c:
            return value + 2
        if startX + 1 == r and startY + 1 == c:
            return value + 3
    
    half = 2**(n-1)
    
    # 1사분면 (좌상단)
    if r < startX + half and c < startY + half:
        return zTraversal(n-1, startX, startY, r, c, value)
    # 2사분면 (우상단)
    elif r < startX + half and c >= startY + half:
        return zTraversal(n-1, startX, startY + half, r, c, value + half**2)
    # 3사분면 (좌하단)
    elif r >= startX + half and c < startY + half:
        return zTraversal(n-1, startX + half, startY, r, c, value + 2 * half**2)
    # 4사분면 (우하단)
    else:
        return zTraversal(n-1, startX + half, startY + half, r, c, value + 3 * half**2)

N, r, c = map(int, sys.stdin.readline().split())
result = zTraversal(N, 0, 0, r, c, 0)
print(result)
