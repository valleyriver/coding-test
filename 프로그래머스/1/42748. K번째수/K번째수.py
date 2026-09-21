def solution(array, commands):
    answer = []
    for start, end, target in commands:
        lst = sorted(array[start - 1:end])
        answer.append(lst[target - 1])
    return answer