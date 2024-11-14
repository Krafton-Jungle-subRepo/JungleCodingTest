import sys
input = sys.stdin.readline

def binarySearch(target):
    st = 0
    en = len(arr) -1
    while(st <= en) :
        # 가운데 값 설정
        mid = (st+en) // 2

        # 중앙값보다 크면 그 이후에서 탐색
        if target > arr[mid] :
            st = mid+1
        # 중앙값보다 작으면 그 전에 탐색
        elif target < arr[mid] :
            en = mid -1
        # 중앙값이면 1 출력 후 종료
        else :
            return 1
    return 0

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

m = int(input())
nums = list(map(int, input().split()))

for k in nums :
    print(binarySearch(k))