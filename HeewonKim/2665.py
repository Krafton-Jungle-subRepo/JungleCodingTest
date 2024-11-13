# 미로만들기
import sys
sys.setrecursionlimit(10**5)

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().rstrip('\n'))) for _ in range(N)]
visited = [([sys.maxsize] * N) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def Dfs(currentX, currentY):
    for i in range(4):
        nextX, nextY = currentX + dx[i], currentY + dy[i]
        if(0<= nextX < N and 0<= nextY < N):
            if(board[nextY][nextX] == 1):
                if(visited[nextY][nextX] > visited[currentY][currentX]):
                    visited[nextY][nextX] = visited[currentY][currentX]
                    Dfs(nextX, nextY)
            else:
                if(visited[nextY][nextX] > visited[currentY][currentX] + 1):
                    visited[nextY][nextX] = visited[currentY][currentX] + 1
                    Dfs(nextX, nextY)

visited[0][0] = 0
Dfs(0, 0)

print(visited[N-1][N-1])