def solution(edges):
    M = 1_000_000  # 노드의 최대 번호를 정의
    
    # 각 노드의 진입차수와 진출차수를 저장할 배열 초기화
    in_deg = [0] * (M + 1)
    out_deg = [0] * (M + 1)
    start = 0  # 탐색 시작 노드
    graph = {}  # 그래프를 인접 리스트 형태로 표현
    donut, stick, eight = 0, 0, 0  # 도넛, 막대, 8자 형태의 개수
    
    # 간선을 통해 그래프를 구성
    for v1, v2 in edges:
        out_deg[v1] += 1  # v1 노드의 진출차수 증가
        in_deg[v2] += 1   # v2 노드의 진입차수 증가
        # v1에서 v2로 향하는 간선을 graph에 추가
        if v1 in graph:
            graph[v1].append(v2)
        else:
            graph[v1] = [v2]
    
    # 시작 노드 찾기: 진입 차수가 없고 진출 차수가 2 이상인 노드
    for i in range(1, M + 1):
        if not in_deg[i] and out_deg[i] >= 2:
            start = i
            break
            
    # 시작 노드에서 이어지는 각 노드 탐색
    for s in graph[start]:
        # 막대의 끝: 진출 차수가 0인 경우
        if out_deg[s] == 0:
            stick += 1
            continue
        
        # 현재 노드부터 탐색 시작
        v = graph[s][0]
        while True:
            # 막대의 끝에 도달한 경우
            if out_deg[v] == 0:
                stick += 1
                break
            # 8자 형태의 중심점: 진출 차수가 2인 노드
            if out_deg[v] == 2:
                eight += 1
                break
            # 도넛 형태의 순환 구조: 시작 노드로 돌아온 경우
            if v == s:
                donut += 1
                break
            
            # 다음 노드로 이동
            v = graph[v][0]
        
    # 결과로 시작 노드, 도넛 개수, 막대 개수, 8자 개수를 리스트로 반환
    return [start, donut, stick, eight]

# 예시 간선 입력
edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(edges))