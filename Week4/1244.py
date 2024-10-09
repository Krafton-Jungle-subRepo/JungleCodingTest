import sys
input = sys.stdin.readline

s = int(input())
switches = [0] + list(map(int, input().split()))
p = int(input())
students = [list(map(int, input().split())) for _ in range(p)]

for gender, num in students:
    if gender == 1:
        for j in range(1, s//num + 1):
            if switches[j*num] == 1:
                switches[j*num] = 0
            else:
                switches[j*num] = 1
    else:
        if num * 2 > s:
            r = s - num
        else:
            r = num - 1
        if switches[num] == 1:
                switches[num] = 0
        else:
                switches[num] = 1
        for i in range(1, r+1):
            if switches[num - i] == switches[num + i]:
                if switches[num-i] == 1:
                    switches[num-i] = switches[num+i] = 0
                else:
                    switches[num-i] = switches[num+i] = 1
            else:
                break
switches.pop(0)

j = 0
for i in range(len(switches)):
    print(switches[i], end=" ")
    j += 1
    if j % 20 ==  0:
        print()
        j = 0