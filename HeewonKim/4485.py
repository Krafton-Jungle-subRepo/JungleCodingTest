# 녹색 옷 입은 애가 젤다지?
import sys
import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
TestCount = 1

def serarchGraph():
    heap = []
    heapq.heappush(heap, [board[0][0], 0, 0])
    visited[0][0] = board[0][0]

    while(heap):
        currnetCost, currentX, currentY = heapq.heappop(heap)
        if(currentX == N-1 and currentY == N-1):
            return currnetCost
        for i in range(4):
            nextX, nextY = currentX+dx[i], currentY+dy[i]
            if(0 <= nextX < N and 0 <= nextY < N and visited[nextY][nextX] > currnetCost + board[nextY][nextX]):
                visited[nextY][nextX] = currnetCost + board[nextY][nextX]
                heapq.heappush(heap, [visited[nextY][nextX], nextX, nextY])

while(1):
    N = int(sys.stdin.readline())
    if(N == 0):
        break
    board = [(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
    visited = [([sys.maxsize] * (N)) for _ in range(N)]
    print(f"Problem {TestCount}: {serarchGraph()}")
    TestCount += 1