# 소용돌이 예쁘게 출력하기
import sys
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
height = abs(r2-r1)+1
width = abs(c2-c1)+1

arr = []
for _ in range(height):
    arr.append([0] * width)

length = 2
value = 1
currentY = 0
currentX = 0
currentDirection = 'R'
max_range = max(abs(r1), abs(r2), abs(c1), abs(c2))
repeat = (max_range * 2 + 1) ** 2


while(value <= repeat):
    if(currentDirection == 'R'):
        for i in range(length-1):
            if(r1<= currentY <= r2 and c1 <= currentX <= c2):
                arr[abs(r1-currentY)][abs(c1-currentX)] = value
            currentX += 1
            value += 1
        currentDirection = 'U'


    elif(currentDirection == 'U'):
        for i in range(length):
            if(r1<= currentY <= r2 and c1 <= currentX <= c2):
                arr[abs(r1-currentY)][abs(c1-currentX)] = value
            currentY -= 1
            value += 1
        currentDirection = 'L'
    
    elif(currentDirection == 'L'):
        currentY += 1
        currentX -= 1
        for i in range(length-1):
            if(r1<= currentY <= r2 and c1 <= currentX <= c2):
                arr[abs(r1-currentY)][abs(c1-currentX)] = value
            currentX -= 1
            value += 1
        currentDirection = 'D'

    elif(currentDirection == 'D'):
        for i in range(length):
            if(r1<= currentY <= r2 and c1 <= currentX <= c2):
                arr[abs(r1-currentY)][abs(c1-currentX)] = value
            currentY += 1
            value += 1
        length += 2
        currentDirection = 'R'

max_value = max(max(row) for row in arr)  # 배열에서 가장 큰 값 찾기
max_width = len(str(max_value))           # 가장 큰 값의 자릿수 계산

for i in range(height):
    for j in range(width):
        print(f"{arr[i][j]:>{max_width}}", end=" ")
    print()  
