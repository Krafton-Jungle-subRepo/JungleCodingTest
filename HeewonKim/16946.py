# 벽 부수고 이동하기 4
import sys
sys.setrecursionlimit(10**6)

# 입력
N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip('\n')))

# 상하좌우
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 방문 처리 배열, 후에 첫번째는 영역의 크기, 두번째는 영역의 id 저장 예정
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
# 영역 id의 인덱스
areaIdx = 1

# Dfs
def Dfs(currentX, currentY, visited, location):
    # 영역 저장 값
    total = 0
    for i in range(4):
        nextX = currentX + dx[i]
        nextY = currentY + dy[i]
        # 다음 영역이 0이고 방문을 아직 하지 않았다면
        if(0<=nextX<M and 0<= nextY<N and board[nextY][nextX] == '0' and visited[nextY][nextX][0] == 0):
            # 방문 처리, 영역 크기를 재귀로 구한 뒤, 영역에 포함되는 위치 location 배열에 추가
            visited[nextY][nextX][0] = 1
            total += Dfs(nextX, nextY, visited, location) + 1
            location.append([nextX, nextY])
    # 영역 크기 반환
    return total

# 이차원 배열을 돌면서
for i in range(N):
    for j in range(M):
        # 현재 위치가 비어있고 방문을 아직 하지 않았다면
        if(board[i][j] == '0' and visited[i][j][0] == 0):
            # 현재 위치와 연결되어 있는 공간을 구함
            location = [[j, i]]
            visited[i][j][0] = 1
            area = Dfs(j, i, visited, location) + 1
            # 현재 공간과 연결되어 있는 위치들에 대해 영역 크기, 영역 ID 변경
            for x, y in location:
                visited[y][x][0] = area
                visited[y][x][1] = areaIdx
            # 영역ID 1 증가
            areaIdx += 1

# 이차원 배열을 돌면서
for i in range(N):
    for j in range(M):
        # 현재가 벽이면
        if(board[i][j] == '1'):
            # res는 상하좌우 영역 크기 합산 결과
            res = 0
            # idxCheck는 상하좌우가 만약 같은 영역일 경우 중복 방지를 위해 영역의 id값을 임시 저장하는 배열
            idxCheck = []
            # 상하좌우를 검사하며
            for k in range(4):
                nextX = j + dx[k]
                nextY = i + dy[k]
                # 배열 내부이며, 처리하지 않은 영역 ID를 가지고 있는 영역일 경우 더해주고, idxCheck에 영역 ID 추가
                if(0<=nextX<M and 0<= nextY<N and visited[nextY][nextX][1] not in idxCheck):
                    idxCheck.append(visited[nextY][nextX][1])
                    res += visited[nextY][nextX][0]
            # 10으로 나눈 res값 출력
            print((res+1) % 10, end='')
        else:
            # 공간일 경우 0 출력
            print(0, end='')
    print()