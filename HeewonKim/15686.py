# 치킨 배달 
import sys
from itertools import combinations

# 치킨집 좌표와, 집의 좌표를 입력받음
N, M = map(int, sys.stdin.readline().split())
houses = []
chicken = []
res = sys.maxsize

for i in range(N):
    inputStr = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if(inputStr[j] == 1):
            houses.append([j, i])
        if(inputStr[j] == 2):
            chicken.append([j, i])

# M개의 치킨집을 조합 라이브러리를 이용하여 선택
tmp = list(combinations(chicken, M))

# 조합의 개수만큼 반봅
for i in range(len(tmp)):
    total = 0
    # 집의 길이만큼 순회
    for j in range(len(houses)):
        tmpsum = sys.maxsize
        # 치킨집의 조합중 선택된 집에 대한 가장 짧은 거리를 계산
        for k in range(M):
            tmpsum = min(tmpsum, abs(houses[j][0]-tmp[i][k][0]) + abs(houses[j][1]-tmp[i][k][1]))
        # 해당 치킨집 조합에 대한 최소 치킨거리 저장
        total += tmpsum
    # 결과 갱신
    res = min(res, total)

print(res)