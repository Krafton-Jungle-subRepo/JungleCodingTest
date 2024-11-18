import sys
input = sys.stdin.readline

N = int(input())
arrA = list(map(int, input().split()))

M = int(input())
arrB = list(map(int,input().split()))

dic = {}

for n in arrA :
    if n in dic :
        dic[n] += 1
    else:
        dic[n] = 1

for m in arrB :
    if m in dic:
        print(dic[m], end=' ')
    else :
        print(0, end=' ')