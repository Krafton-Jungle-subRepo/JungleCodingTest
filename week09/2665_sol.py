import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

def sol():
    heap = [(0, 0, 0)]  # (흰 방으로 바꾼 횟수, x, y)
    cnt[0][0] = 0

    while heap:
        change, x, y = heapq.heappop(heap)

        if x == N-1 and y == N-1:
            return change

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                next_change = change + (rooms[nx][ny] == '0')
                
                if cnt[nx][ny] > next_change:
                    cnt[nx][ny] = next_change
                    heapq.heappush(heap, (next_change, nx, ny))

N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rooms = [input().strip() for _ in range(N)]
cnt = [[INF] * N for _ in range(N)]

result = sol()
print(result)
