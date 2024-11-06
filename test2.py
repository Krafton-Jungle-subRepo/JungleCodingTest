def initSkip(p):
    NUM = 27  # 알파벳 수
    M = len(p) # 패턴의 길이
    skip = [M for i in range(NUM)] #skip 함수를 모두 M값으로 초기화
    for i in range(M):
        skip[ord(p[i]) - ord('A')] = M - i - 1 
    return skip # skip 배열 반환

print(initSkip("ATION")) # 임시로 ATION 이란 패턴을 입력

def BM(p, t):
    M = len(p)
    N = len(t)
    skip = initSkip(p)

    i = M-1
    j = M-1

    while j >= 0:
        while t[i] != p[j]:
            k = skip[ord(t[i]) - ord('A')]
            if M - j > k:
                i = i + M - j
            else:
                i = i + k
            if i >= N:
                return N
            j = M - 1
        i = i-1
        j = j-1
    return i+1

print(BM("ATION","VISOINQUESTIONONIONCAPTIONGRADUATION"))