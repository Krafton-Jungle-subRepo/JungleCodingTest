def sol(A, N, K):
    # 각 K 길이의 구간 합을 계산 (슬라이딩 윈도우)
    window_sums = [0] * (N - K + 1)
    current_sum = sum(A[:K])
    window_sums[0] = current_sum

    for i in range(1, N - K + 1):
        current_sum += A[i + K - 1] - A[i - 1]
        window_sums[i] = current_sum

    # 최대 합 계산 (겹치지 않는 두 구간)
    max_left = [0] * (N - K + 1)  # 왼쪽에서 i까지의 최대 합
    max_left[0] = window_sums[0]

    for i in range(1, N - K + 1):
        max_left[i] = max(max_left[i - 1], window_sums[i])

    max_right = [0] * (N - K + 1)  # 오른쪽에서 i부터의 최대 합
    max_right[-1] = window_sums[-1]

    for i in range(N - K - 1, -1, -1):
        max_right[i] = max(max_right[i + 1], window_sums[i])

    # 겹치지 않는 두 구간 합의 최대값 찾기
    max_total = float('-inf')
    for i in range(N - 2 * K + 1):
        max_total = max(max_total, max_left[i] + max_right[i + K])

    return max_total


# 입력 처리 및 출력
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = sol(A, N, K)
    print(f"#{t} {result}")
