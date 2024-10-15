import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def divide(x):
    front = []
    back = []
    is_same = True

    if len(x) == 3:
        if x[0] != x[2]:
            return True
        else:
            return False
    elif len(x) == 1:
        return True

    else:
        center = (len(x)-1) // 2
        for i in range(len(x)):
            if i < center:
                front.append(int(x[i]))
            elif i > center:
                back.append(int(x[i]))
        for i in range(len(front)):
            if front[i] == back[len(back)-1-i] :
                is_same = False
        if is_same:
            if len(front) <= 3:
                return (divide(front) and divide(back))
            return (divide(front) and divide(back))
        else:
            return False

    
T = int(input())

for i in range(T):
    folds = list(str(input().rstrip()))
    if divide(folds):
        print("YES")
    else:
        print("NO")