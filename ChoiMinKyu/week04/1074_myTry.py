# 1074 Z
# 2차원 배열을 직접 Z 형태로 순회하며 채우는 방식으로 문제 해결.
# 메모리 초과로 실패 :: 2차원 배열로 직접 구현 시 2^N * 2^N
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# z형태로 2차원 배열을 채우는 함수
def zTraversal(n, startX, startY, arr):
    # 배열 요소 값 전역 변수로 선언
    global value

    # n이 1일 때, z 형태로 순회하며 배열 채움 
    if (n == 1):
        for i in range(4):
            nx = startX+dx[i%4]
            ny = startY+dy[i%4]
            arr[nx][ny] = value
            value += 1
    # n이 1보다 클 때, 재귀적으로 함수 호출
    else:
        zTraversal(n-1, 0 , 0, arr)
        zTraversal(n-1, 0 , 2**(n-1),arr)
        zTraversal(n-1, 2**(n-1) , 0,arr)
        zTraversal(n-1, 2**(n-1) , 2**(n-1),arr)

# 정수 N, r, c 입력
N,r,c = map(int, input().split())
# 사이즈 계산 후 배열 생성
size = 2**N
arr = [[0]*size for _ in range(size)]
# 배열 요소로 할당할 값
value = 0
# 배열 안에서 인덱스의 움직임을 구현 할 deltaX, deltaY
dx = [0,0,1,1]
dy = [0,1,0,1]
# 함수 호출
zTraversal(N, 0, 0, arr)
# 결과 출력
print(arr[r][c])