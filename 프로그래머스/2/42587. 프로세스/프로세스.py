from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque()
    count = 0
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
        
    while queue:
        index, priority = queue.popleft()
        if len(queue) == 0 or priority >= max(item[1] for item in queue):
            count += 1
            if index == location:
                answer = count
                break
        else:
            queue.append((index, priority))
    
    return answer