def solution(a, b):
    answer = 0
    start = min(a, b)
    end = max(a, b) + 1
    for number in range(start, end):
        answer += number
    return answer