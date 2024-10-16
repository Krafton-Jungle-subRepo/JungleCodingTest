# RGB거리 2
import sys

# 입력
N = int(sys.stdin.readline())
house = [(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
# 결과 출력할 변수
res = sys.maxsize

# 시작 색(color)을 정하는 반복문
for color in range(3):
    # dp 배열 선언 및, 시작 값 초기화
    dp = [[sys.maxsize,sys.maxsize,sys.maxsize] for _ in range(N)]
    dp[0][color] = house[0][color]

    # 1부터 N까지 반복하며, 현재색이 아닌 두 값의 결과중 최소인 값을 선택, 저장
    for i in range(1, N):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]
    
    # 시작값과 똑같지 않다면, res에 최솟값 비교하여 저장
    for i in range(3):
        if(color != i):
            res = min(res, dp[N-1][i])

# 결과 출력
print(res)