# 빠른 입력 위해 sys.stdin 사용
import sys
import math
import heapq
input = sys.stdin.readline

# N 입력
N = int(input())
flowers= []

# 꽃 정보 입력
for _ in range(N):
    # 꽃 피는 날짜 start, 지는 날짜 end 입력
    sm,sd,em,ed = map(int,input().split())
    # start, end를 3~4자리 정수로 치환
    start = sm*100+sd
    end = em*100+ed
    # 필요없는 날짜 정보는 받지 않음
    if 300<end and start<1200:
        flowers.append((start,end))

# 꽃 정렬 (개화 날짜 기준 오름차순 정렬 후 지는 날짜 기준 오름차순)
flowers.sort(key= lambda x:(x[0],x[1]))

# 최종적으로 합산 후 꽃이 지는 날짜(시작은 3월1일)
end_date = 301
# 결과 할당할 변수
count = 0

# flowers 리스트에 값이 남아있는 동안 반복
while flowers:
    # 종료 조건: 최종 합산 후 꽃이 지는 날짜가 11월30일 이후거나 중간에 이어지지 않으면 종료
    if end_date >= 1201 or flowers[0][0] > end_date:
        break

    tmp = -1
    for _ in range(len(flowers)):
        # 개화 날짜가 현재 합산 지는 날짜보다 빠른 경우 중
        if flowers[0][0] <= end_date:
            # 가장 느리게 지는 꽃을 선택.
            if tmp <= flowers[0][1]:
                tmp = flowers[0][1]
            # 조건 확인 한 꽃은 배열에서 삭제
            flowers.remove(flowers[0])
        
        else:
            break
    # 최종 합산 꽃이 지는 날짜 업데이트하고 결괏값 +1
    end_date = tmp
    count += 1
# 중간에 끊긴 경우, 조건에 부합하지 않으므로 0 출력
if end_date < 1201:
    print(0)
# 결과 출력
else:
    print(count)