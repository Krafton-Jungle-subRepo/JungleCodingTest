# 빠른 입력 위해 sys.stdin 사용
import sys
import math
import heapq
input = sys.stdin.readline

# N 입력
N = int(input())
flowers= []

# 꽃 입력
for _ in range(N):
    # 꽃 피는 날짜 start, 지는 날짜 end 입력
    sm,sd,em,ed = map(int,input().split())
    # start, end를 3~4자리 정수로 치환
    start = sm*100+sd
    end = em*100+ed
    # 필요없는 날짜 정보는 받지 않음
    if 300<end and start<1200:
        flowers.append((start,end))

# 꽃 정렬 (개화 날짜 기준 오름차순)
flowers.sort(key= lambda x:(x[0],x[1]))

end_date = 301
count = 0

while flowers:
    if end_date >= 1201 or flowers[0][0] > end_date:
        break

    tmp = -1

    for _ in range(len(flowers)):
        print(tmp)
        
        if flowers[0][0] <= end_date:
            if tmp <= flowers[0][1]:
                tmp = flowers[0][1]
            
            flowers.remove(flowers[0])
        
        else:
            break
    
    end_date = tmp
    count += 1

if end_date < 1201:
    print(0)
else:
    print(count)