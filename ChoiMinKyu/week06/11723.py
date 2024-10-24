import sys
input = sys.stdin.readline

M = int(input())
S = set([])

for i in range(M):

    ins = input().rstrip()
    n = 0

    if ins != 'all' and ins != 'empty':
        ins, n = ins.split()
        n = int(n)
    
    if ins == 'add':
        S.add(n)
    
    if ins == 'remove':
        if n in S:
            S.remove(n)
    
    if ins == 'check':
        if n in S:
            print(1)
        else:
            print(0)
    
    if ins == 'toggle':
        if n in S:
            S.remove(n)
        else:
            S.add(n)
    
    if ins == 'all':
        S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    
    if ins == 'empty':
        S = set()