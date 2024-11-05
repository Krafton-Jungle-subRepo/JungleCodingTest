# A와 B
import sys
S = list(sys.stdin.readline().rstrip('\n'))
T = list(sys.stdin.readline().rstrip('\n'))

while(len(T) > len(S)):
    if(T[-1] == 'A'):
        T.pop()
    else:
        T.pop()
        T.reverse()

if(T == S):
    print(1)
else:
    print(0)