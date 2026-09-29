def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(now):
        visited[now] = 1
        
        for next_node in range(n):
            if visited[next_node] == 1:
                continue
            if computers[now][next_node] == 0:
                continue
                
            dfs(next_node)   
    
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            dfs(i)

    return answer