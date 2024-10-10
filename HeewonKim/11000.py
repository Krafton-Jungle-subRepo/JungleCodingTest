# 강의실 배정
import sys
import heapq

# 입력받은 후 정렬
N = int(sys.stdin.readline())
lectures = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    lectures.append([start, end])
lectures.sort()

# 힙 저장할 배열 선언 및 초기값으로 첫 수업의 끝난느 시간 삽입
heap = []
heapq.heappush(heap, lectures[0][1])

# 두번째 끝까지
for i in range(1, N):
    # 현재 강의 시작, 종료시간
    currentStart, currentEnd = lectures[i]

    # 힙에 들어있는 강의중 끝나는 시간이 가장 빠른 것과 현재의 시작시간을 비교
    # 힙의 강의 종료시간과 현재 시작시간중 시작시간이 더 작다면 새로운 강의실 필요
    if(heap[0] > currentStart):
        heapq.heappush(heap, currentEnd)

    # 그렇지 않다면 기존 강의실 종료시간 최신화
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, currentEnd)

# 힘의 길이 출력
print(len(heap))