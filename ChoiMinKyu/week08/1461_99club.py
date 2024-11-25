# 빠른 입력을 위해 stdin 사용
import sys
input = sys.stdin.readline
# 입력 처리
N,M = map(int,input().split())
books = list(map(int,input().split()))

positive = []
negative = []
last = 0
# books 리스트에서 양수값, 음수값을 각각 리스트로 분할
# 절대값이 가장 큰 값을 last 변수로 할당
for book in books:
  last = max(abs(book),last)
  if book > 0:
    positive.append(book)
  elif book < 0:
    negative.append(book*-1)
# 각 리스트를 내림차순 정렬
positive.sort(reverse=True)
negative.sort(reverse=True)
# M칸 씩 건너뛰면서 값을 2번씩 더함
result = 0
for i in range(0,len(positive),M):
  result += positive[i]*2

for i in range(0,len(negative),M):
  result += negative[i]*2
# result에서 last값 빼줌
result -= last
# 결과 출력
print(result)