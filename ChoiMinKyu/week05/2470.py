import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int,input().split()))
solutions.sort()

left = 0
right = N-1

best_mix = sys.maxsize
best_left = 0
best_right = 0

while (left < right):
    mix = solutions[left] + solutions[right]
    if (abs(mix) < abs(best_mix)):
        best_mix = mix
        best_left = left
        best_right = right
    
    if mix < 0:
        left += 1
    else:
        right -= 1

print(solutions[best_left],solutions[best_right])