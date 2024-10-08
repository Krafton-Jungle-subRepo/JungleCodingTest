# 2477 - 숫자의 개수
import sys
input = sys.stdin.readline

# A,B,C 입력
A = int(input())
B = int(input())
C = int(input())
# A*B*C 결괏값을 문자열로 변환
res = str(A*B*C)
# tmp 리스트를 이용해 각 자리수의 개수 할당
tmp = [0] * 10
for i in range(len(res)):
    tmp[int(res[i])] += 1
# 결과 출력
for result in tmp:
    print(result)