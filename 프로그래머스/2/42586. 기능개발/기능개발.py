from collections import deque


def solution(progresses, speeds):
    answer = []
    queue = deque()
    count = 0
    for i in range(len(progresses)):
        left = 100 - progresses[i]
        if left % speeds[i] == 0:
            day = left // speeds[i]
        else:
            day = left // speeds[i] + 1
        queue.append((i, day))
    
    while queue:
        index, day = queue.popleft()
        count += 1
        while queue:
            next_index, next_day = queue.popleft()
            if next_day <= day:
                count += 1
            else:
                queue.appendleft((next_index, next_day))
                break
        answer.append(count)
        count = 0
        
    return answer