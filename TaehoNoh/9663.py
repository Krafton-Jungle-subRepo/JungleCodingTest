import sys
input = sys.stdin.readline

N = int(input())

board = [0 for _ in range(N)]
count = 0

# 주어진 행 y에서 퀸을 안전하게 배치할 수 있는지 확인하는 함수
def checkPlace(y):       
    for i in range(y):   # 이전 행들을 검사
        # 같은 열에 다른 퀸이 있거나 대각선에 다른 퀸이 있는지 확인
        if(board[y] == board[i] or abs(board[y] - board[i]) == abs(y-i)) :    
            return False        # 배치할 수 없으면 False 반환
    return True                 # 안전하게 배치할 수 있으면 True 반환


def placeQuuen(y):
    global count                # 전역 변수 count 사용

    if(y == N):                 # 모든 퀸이 성공적으로 배치된 경우
        count += 1              # 경우의 수 증가
    else :
        for i in range(N):      # 현재 행 y에서 모든 열 시도
            board[y] = i        # 퀸을 현재 열 i에 배치
            if(checkPlace(y)):  # 안전한지 확인
                placeQuuen(y+1) # 다음 행으로 재귀 호출
            board[y] = 0

placeQuuen(0)                   # 첫번째 행에서 퀸 배치 시작
print(count)                    # 가능한 퀸 배치 경우의 수 출력