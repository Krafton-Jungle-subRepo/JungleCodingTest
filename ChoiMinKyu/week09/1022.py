r1, c1, r2, c2 = map(int,input().split())

# 우 / 상 / 좌 / 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 반복문 범위부터 설정
rLength = r2-r1
cLength = c2-c1
# r1,r2,c1,c2 중 0 있으면 이것도 인덱스로 쳐서 더해줘야함
if r1 == 0 and r2 != 0:
  rLength += 1
if r2 == 0 and r1 != 0:
  rLength += 1
if c1 == 0 and c2 != 0:
  cLength += 1
if c2 == 0 and c1 != 0:
  cLength += 1

# arr 배열 생성, 0으로 초기화
arr = list([0]*(cLength) for _ in range(rLength))

# 시작 x,y 설정
startX = startY = 0

if r1 < 0:
  startX = -r1


startY = 0

for i in range(rLength):
  for j in range(cLength):
    arr[i+abs(r1)] = n
    