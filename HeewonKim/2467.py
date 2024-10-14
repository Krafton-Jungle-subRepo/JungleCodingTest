# 용액
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

leftIdx = 0
rightIdx = N-1
res = sys.maxsize
resLeft = arr[0]
resRight = arr[N-1]

while(leftIdx != rightIdx):
    if(abs(arr[leftIdx] + arr[rightIdx]) < res):
        res = abs(arr[leftIdx] + arr[rightIdx])
        resLeft = arr[leftIdx]
        resRight = arr[rightIdx]

    if(arr[leftIdx] + arr[rightIdx] > 0):
        rightIdx -= 1
    else:
        leftIdx -= 1

print(resLeft, resRight)