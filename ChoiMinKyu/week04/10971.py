# 10971 - 외판원 순회 2

import sys
input = sys.stdin.readline

# dfs로 문제 해결
def dfs(start,next_,cost,visited):

    # 최소 비용 전역변수로 선언
    global min_cost

    # 전체 노드를 모두 방문했을 때
    if 0 not in visited:
        # 다시 start 노드로 돌아올 수 있는 경로가 있다면
        if costs[next_][start] > 0:
            # 마지막 도시 -> 다시 출발지로 오는 비용 합쳐 최소 비용 갱신
            min_cost = min(min_cost, cost+costs[next_][start])
        return min_cost
    # 모든 노드들에 대해 순회
    for i in range(N):
        # 노드 연결 여부, 방문 여부, 비용 최소 비용보다 큰지 확인
        if (costs[next_][i] > 0) and (visited[i] == 0) and (cost < min_cost):
            # 방문 표시하고 dfs 재귀 호출
            visited[i] = 1
            dfs(start, i, cost+costs[next_][i],visited)
            # dfs 순회 종료 후 다시 방문 해제
            visited[i] = 0


# 도시 입력
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
# min_cost의 선언 값을 maxsize로 설정
min_cost = sys.maxsize

# 모든 도시에 대해 반복 수행
for i in range(N):
    visited = [0] * N
    visited[i] = 1
    dfs(i,i,0,visited)
# 결과 출력
print(min_cost)