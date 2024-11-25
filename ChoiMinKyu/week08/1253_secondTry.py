import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
### 정렬을 꼭 해주는 습관을 들이자
A.sort()

cnt = 0
for i in range(N):
  goal = A[i]
  # 두 포인터 start, end 세팅
  start = 0
  end = N-1

  while (start < end):
    # 칮은 경우
    if goal == A[start] + A[end]:
      ### 값에 본인 포함 예외처리
      # start의 값이 본인 값이면 
      if start == i:
        start += 1
      # end의 값이 본인 값이면
      elif end == i:
        end -= 1
      # 그냥 순수하게 정답을 찾았다면
      else:
        cnt += 1
        break
    # 부분합이 크다면
    elif goal < A[start] + A[end]:
      end -= 1
    # 부분합이 작다면
    elif goal > A[start] + A[end]:
      start += 1
# 결과 출력
print(cnt)