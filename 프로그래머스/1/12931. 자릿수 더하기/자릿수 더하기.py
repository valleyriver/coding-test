def solution(n):
    answer = 0
    s = str(n)
    for char in s:
        answer += int(char)
    return answer