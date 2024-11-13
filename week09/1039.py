# 교환
from collections import deque
N, K = map(int, input().split())
M = len(str(N))


def bfs(N, K):
    visited = set()
    visited.add((N, 0))
    q = deque()
    q.append((N, 0))
    answer = 0
    while q:
        n, k = q.popleft()
        # 같은 depth 안에서는 최댓값을 answer로 갱신
        if k == K:
            answer = max(answer, n)
            continue
        # n을 문자열 리스트로 변환
        n = list(str(n))
        # 이중 for문 내에서 순서 바꿈
        for i in range(M-1):
            for j in range(i+1, M):
                # 맨 첫 글자가 0이 되면 skip
                if i == 0 and n[j] == '0':
                    continue
                # swap여기서
                n[i], n[j] = n[j], n[i]
                nn = int(''.join(n))
                if (nn, k+1) not in visited:
                    q.append((nn, k+1))
                    visited.add((nn, k+1))
                n[i], n[j] = n[j], n[i]
    return answer if answer else -1


print(bfs(N, K))