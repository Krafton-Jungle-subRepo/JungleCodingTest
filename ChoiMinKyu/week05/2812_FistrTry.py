import sys
input = sys.stdin.readline

N,K = map(int,input().split())
numArr = [int(d) for d in input().rstrip()]
result = ''

for i in range(K):
    index = numArr.index(min(numArr))
    numArr.pop(index)

for i in range(len(numArr)):
    result += str(numArr[i])

print(int(result))