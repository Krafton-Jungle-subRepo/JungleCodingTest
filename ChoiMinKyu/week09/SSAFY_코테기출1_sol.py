def find_kth_pair_sum(N, K, sequence):
    # 모든 가능한 쌍을 생성
    pairs = [(a, b) for a in sequence for b in sequence]
    
    # 쌍을 정렬: 첫 번째 원소를 기준으로, 같으면 두 번째 원소로 정렬
    pairs.sort()
    
    # K번째 쌍을 선택하고, 합을 계산하여 반환
    kth_pair = pairs[K - 1]
    return sum(kth_pair)


# 입력 처리
T = int(input())  # 테스트 케이스 수
results = []
for t in range(1, T + 1):
    # 각 테스트 케이스 입력
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    # K번째 쌍의 합을 구하여 결과에 저장
    result = find_kth_pair_sum(N, K, sequence)
    print(f"#{t} {result}")