answer = 0
def DFS(k, cnt, dungeons, visited):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if visited[i] == 0 and k >= dungeons[i][0]:       
            visited[i] = 1
            DFS(k-dungeons[i][1], cnt+1, dungeons, visited)
            visited[i] = 0
    

def solution(k, dungeons):
    # answer = 0
    global answer
    visited = [0]*len(dungeons)       # 방문 여부 체크하는 배열
    
    # cnt: 탐험한 던전 개수, k: 남은 피로도
    DFS(k, 0, dungeons, visited)     # 0: 방문한 던전의 개수를 0으로 DFS 함수에 넘겨준다.
    
    return answer

k = 80 # 현재 피로도
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k,dungeons))