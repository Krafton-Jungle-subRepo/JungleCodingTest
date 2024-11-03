# 빠른 입력을 위해 sys.stdin 사용
import sys
input = sys.stdin.readline
# 꽃 개수 입력
N = int(input())
flowers = []
# 꽃 정보 입력
for _ in range(N):
    sm, sd, em, ed = map(int,input().split())
    # 날짜 정보를 3, 4자릿수 정수로 변환 해 리스트에 저장
    start = sm*100+sd
    end = em*100+ed
    flowers.append((start,end))
# 꽃 정보 정렬 (개화 시작 날짜 오름차순 정렬 후 지는 날짜 기준으로 오름차순 정렬)
flowers.sort(key = lambda x:(x[0],x[1]))
# 최종 합산 지는 날짜: 시작 할 때는 3월 1일
end_date = 301
# 결과 할당할 변수
result = 0
# flowers 배열에 값이 남아있는 동안 반복
while flowers:
    # 종료 조건: 최종 합산 날짜가 12월 01일 이상이거나, 중간에 이어지지 않는 경우
    if (end_date >= 1201 or flowers[0][0] > end_date):
        break

    tmp = -1
    for i in range(len(flowers)):
        # 개화 날짜가 최종 합산 지는 날짜보다 작은 꽃 중에서
        if flowers[0][0] <= end_date:
            # 가장 늦게 지는 꽃을 선택
            if tmp <= flowers[0][1]:
                tmp = flowers[0][1]
            # 조건 확인한 꽃은 리스트에서 제거
            flowers.remove(flowers[0])
        # 중간에 안이어지면 break
        else:
            break
    # 최종 합산 지는 날짜 업데이트
    end_date = tmp
    # 결괏값 +1
    result += 1
# 중간에 이어지지 않은 경우 0 출력
if end_date< 1201:
    print(0)
# 결과 출력
else:
    print(result)
    