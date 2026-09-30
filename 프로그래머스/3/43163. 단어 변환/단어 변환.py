from collections import deque


def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    queue = deque()
    
    if target not in words:
        return 0
    
    queue.append((begin, 0))
    
    while queue:
        now, count = queue.popleft()
        
        for i, word in enumerate(words):
            if visited[i] == 1:
                continue
                
            diff_count = 0
            
            for j in range(len(word)):
                if now[j] != word[j]:
                    diff_count += 1
                    
                    if diff_count > 1:
                        break
                        
            if diff_count == 1:
                if word == target:
                    answer = count + 1
                    return answer
                
                visited[i] = 1
                queue.append((word, count + 1))
                
    return answer