def solution(n, m, x, y, r, c, k):
    import sys 
    sys.setrecursionlimit(10**5)
    global answer
    answer = ''

    def Dfs(currentX, currentY, count, move):
        global answer
        if(answer != ''):
            return
        
        remaining_moves = k - count
        distance_to_goal = abs(currentX - c) + abs(currentY - r)

        if(remaining_moves < distance_to_goal or (remaining_moves - distance_to_goal) % 2 != 0):
            return
        if(count == k):
            if(currentX == c and currentY == r):
                answer = move
            return 

        if(currentY+1 <= n):
            Dfs(currentX, currentY+1, count+1, move+'d')
        if(currentX-1 >= 1):
            Dfs(currentX-1, currentY, count+1, move+'l')
        if(currentX+1 <= m):
            Dfs(currentX+1, currentY, count+1, move+'r')
        if(currentY-1 >= 1):
            Dfs(currentX, currentY-1, count+1, move+'u')

    Dfs(y, x, 0, '')

    if(answer == ''):
        answer = "impossible"
    
    return answer

