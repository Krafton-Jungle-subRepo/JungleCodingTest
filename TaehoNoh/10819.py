import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
answer = 0
visited = [False] * n

def dfs(li):
    global answer
    if len(li) == n :
        sum = 0
        for i in range(n-1) :
            sum += abs(li[i] - li[i+1])
        answer = max(answer, sum)
        return
    
    for next in range(len(arr)) :
        if not visited[next] :
            visited[next] = True
            li.append(arr[next])
            dfs(li)
            visited[next] = False
            li.pop()

dfs([])

print(answer)
