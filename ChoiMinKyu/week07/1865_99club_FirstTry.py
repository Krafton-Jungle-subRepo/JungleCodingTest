# 빠른 입력 위해 stdin 사용
import sys
input = sys.stdin.readline
# 최대값 = 시스템 최대값 사용
INF = sys.maxsize

# bellmanFord 함수 정의
def bellmanFord(start):
    # 시작 지점 거리 0으로 설정
    distance[start] = 0
    # N-1번 반복
    for _ in range(N-1):
        # 간선 꺼내기
        for curr, next, cost in edges:
            # 시작 노드 + 비용 더한 값이 현재 비용보다 작다면 배열 갱신
            if (distance[curr] != INF and distance[next] > distance[curr] + cost):
                distance[next] = distance[curr] + cost
    # 음수 루프가 존재하는지 확인, 있으면 True 리턴
    for curr, next, cost in edges:
        if distance[curr] != INF and distance[next] > distance[curr] + cost:
            return True
    # 없으면 False 리턴 
    return False
        

# 테스트 케이스
TC = int(input())

for _ in range(TC):
    # 지점 수 N, 도로 수 M, 웜홀 수 W
    N,M,W = map(int,input().split())
    # 비용 배열을 최댓값으로 초기화.
    distance = [INF] * (N+1)
    # 간선을 할당할 배열
    edges = []

    # 도로 정보 입력
    for _ in range(M):
        S,E,T = map(int,input().split())
        edges.append((S,E,T))
        edges.append((E,S,T))
    
    # 웜홀 정보 입력 (웜홀을 음수 가중치를 가진 도로로 취급)
    for _ in range(W):
        S,E,T = map(int,input().split())
        edges.append((S,E,-T))
    # 가능 여부 할당할 플래그
    is_possible = False
    # 모든 지점에 대해 출발
    for start in range(1, N+1):
        # distance 초기화
        distance = [INF] * (N+1)
        # bellmanFord 수행 중 음수 루프가 존재한다면 플래그 True로
        if bellmanFord(start):
            is_possible = True
            break
    # 결과 출력
    print("YES" if is_possible else "NO")