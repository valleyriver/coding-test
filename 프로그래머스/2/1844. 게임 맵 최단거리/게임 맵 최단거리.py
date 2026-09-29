from collections import deque


def solution(maps):
    answer = -1
    end_y, end_x = len(maps) - 1, len(maps[0]) - 1
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    queue = deque()
    
    visited[0][0] = 1
    queue.append((0, 0, 1))
    
    while queue:
        y, x, distance = queue.popleft()
        
        if y == end_y and x == end_x:
            answer = distance
            break
            
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny > end_y or nx > end_x:
                continue
            if maps[ny][nx] == 0:
                continue
            if visited[ny][nx] == 1:
                continue
                
            visited[ny][nx] = 1
            queue.append((ny, nx, distance + 1))
        
    return answer