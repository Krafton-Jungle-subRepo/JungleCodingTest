answer = 0

def dfs(k,cnt,visited,dungeons):
  global answer
  answer = max(answer,cnt)

  for i in range(len(dungeons)):
    if visited[i] == 0 and k >= dungeons[i][0]:
      visited[i] = 1
      dfs(k-dungeons[i][1],cnt+1,visited,dungeons)
      visited[i] = 0

def solution(k, dungeons):
  global answer

  visited = [0]*len(dungeons)
  dfs(k,0,visited,dungeons)

  return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k,dungeons))