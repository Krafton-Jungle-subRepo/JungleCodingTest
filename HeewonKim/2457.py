import sys
import heapq

def changeDay(Month, Day):
    total = 0
    for i in range(1, Month):
        if(i == 4 or i == 6 or i == 9 or i == 11):
            total += 30
        elif(i == 2):
            total += 28
        else:
            total += 31
    return total + Day

N = int(sys.stdin.readline())
flowers = []

# 꽃 정보 입력 및 날짜 변환
for _ in range(N):
    startMonth, startDay, endMonth, endDay = map(int, sys.stdin.readline().split())
    start = changeDay(startMonth, startDay)
    end = changeDay(endMonth, endDay)
    flowers.append((start, end))

# 시작일 기준 정렬, 시작일이 같다면 종료일을 기준으로 내림차순 정렬
flowers.sort(key=lambda x: x[0])

currentEnd = changeDay(3, 1)
EndTerm = changeDay(11, 30)
res = 0
heap = []
idx = 0

# 정원 피는 기간 유지하기 위해 탐색 시작
while currentEnd < EndTerm:
    # 현재 범위 내에서 피는 꽃을 힙에 추가
    while idx < N and flowers[idx][0] <= currentEnd:
        heapq.heappush(heap, -flowers[idx][1])  # 종료일의 최대값을 얻기 위해 음수로 저장
        idx += 1
    # 힙이 비어있다면 더 이상 범위를 확장할 수 없으므로 종료
    if not heap:
        res = 0
        break
    # 가장 늦게 지는 꽃을 선택하여 현재 범위를 확장
    currentEnd = -heapq.heappop(heap)
    res += 1

# 최종적으로 EndTerm을 덮었는지 확인
if currentEnd < EndTerm:
    res = 0
print(res)
