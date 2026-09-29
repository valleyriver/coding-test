def solution(numbers, target):
    answer = 0
    
    def dfs(level, total):
        nonlocal answer
        if level == len(numbers):
            if total == target:
                answer += 1
            return
        dfs(level + 1, total + numbers[level])
        dfs(level + 1, total - numbers[level])
        
    dfs(0, 0)
    return answer