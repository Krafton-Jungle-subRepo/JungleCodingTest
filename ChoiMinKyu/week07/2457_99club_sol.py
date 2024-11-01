import sys
input = sys.stdin.readline

N = int(input())
flowers = []

for _ in range(N):
    sm, sd, em, ed = map(int,input().split())
    start = sm*100+sd
    end = em*100+ed
    flowers.append((start,end))

flowers.sort(key = lambda x:(x[0],x[1]))

end_date = 301
result = 0

while flowers:
    if (end_date >= 1201 or flowers[0][0] > end_date):
        break

    tmp = -1
    for i in range(len(flowers)):
        if flowers[0][0] <= end_date:
            if tmp <= flowers[0][1]:
                tmp = flowers[0][1]
            flowers.remove(flowers[0])
        
        else:
            break
    
    end_date = tmp
    result += 1

if end_date< 1201:
    print(0)
else:
    print(result)
    