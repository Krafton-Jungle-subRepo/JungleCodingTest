# 좌표 (i, j)에 해당하는 값을 반환하는 함수 f(i, j)
def f(i, j):
    # 나선의 현재 레벨 n을 계산 (i와 j의 절댓값 중 큰 값)
    n = max(abs(i), abs(j))
    # (n, n) 위치의 값을 계산하는 기본 값 val (나선의 끝 값)
    val = (2 * n + 1) ** 2
    
    # 각 면에 따라 값이 감소할 양을 설정
    diff = 2 * n
    # 상단 면 (오른쪽 끝에서 위쪽으로)
    if i == n:
        return val - (n - j)
    val -= diff
    # 왼쪽 면 (위쪽 끝에서 왼쪽으로)
    if j == -n:
        return val - (n - i)
    val -= diff
    # 하단 면 (왼쪽 끝에서 아래쪽으로)
    if i == -n:
        return val - (j + n)
    val -= diff
    # 오른쪽 면 (아래쪽 끝에서 오른쪽으로)
    return val - (i + n)

# 주어진 값의 자릿수를 계산하는 함수 g(val)
def g(val):
    # 절댓값을 문자열로 변환해 길이를 계산하여 자릿수 반환
    return len(str(abs(val))) if val != 0 else 1


# 사용자로부터 출력할 좌표의 범위 (r1, c1)부터 (r2, c2)까지 입력 받음
r1, c1, r2, c2 = map(int, input().split())

# 가장 큰 자릿수를 저장할 변수 k를 0으로 초기화
k = 0
# 지정된 좌표 범위 내 모든 위치에 대해 f(i, j) 값을 계산
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        # f(i, j)의 자릿수를 계산하여 최댓값을 k에 저장
        k = max(k, g(f(i, j)))

# 지정된 좌표 범위 내의 값을 출력 (값을 k의 너비에 맞춰 정렬)
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        # 오른쪽 정렬하여 너비 k만큼 공간을 차지하도록 출력
        print(f"{f(i, j):>{k}}", end=" ")
    # 각 행의 출력이 끝나면 줄바꿈
    print()
