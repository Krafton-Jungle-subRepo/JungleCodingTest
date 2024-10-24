import sys
import bisect
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

# arr 복사
arr2 = []
# arr 오름차순 정렬 
arr2.extend(set(arr))

arr2.sort()

dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end=' ')