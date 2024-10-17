# 세 용액
import sys

# 입력 및 정렬
N = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()
res = [sys.maxsize, sys.maxsize, sys.maxsize]

# start 설정
for start in range(N-1):
    # mid, end 설정
    mid = start + 1
    end = N-1
    # mid와 end가 같지 않을때까지
    while(mid != end):
        # res와 값 비교, 갱신
        if(abs(sum(res)) > abs(liquid[start]+liquid[mid]+liquid[end])):
            res = [liquid[start], liquid[mid], liquid[end]]
        
        # 현재 값이 0보다 크면 end 1 감소
        if(liquid[start]+liquid[mid]+liquid[end] > 0):
            end -= 1
        # 현재 값이 0보다 작으면 start 1 증가
        elif(liquid[start]+liquid[mid]+liquid[end]  < 0):
            mid += 1
        # 합이 0일때는 중단
        else:
            break
# 출력
print(' '.join(map(str, res)))
   
