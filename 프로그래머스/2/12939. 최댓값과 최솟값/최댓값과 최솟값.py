def solution(s):
    min_value = 21e8
    max_value = -21e8
    lst = list(map(int, s.split()))
    for item in lst:
        if item < min_value:
            min_value = item
        if item > max_value:
            max_value = item
    answer = f'{min_value} {max_value}'
    return answer