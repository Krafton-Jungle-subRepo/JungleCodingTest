import sys
input = sys.stdin.readline

# 테스트 케이스 입력
T = int(input())
# 테스트 케이스만큼 반복
for _ in range(T):
    # 문자열 입력
    answer = input().rstrip()
    # tmp를 이용해 연속 정답 처리, record에 최종 결괏값 할당
    record = 0
    tmp = 0
    for ans in answer:
        if ans == 'O':
            tmp += 1
            record += tmp
        if ans == 'X':
            tmp = 0
    # 결과 출력
    print(record)