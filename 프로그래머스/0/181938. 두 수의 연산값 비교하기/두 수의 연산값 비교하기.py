def solution(a, b):
    num1 = int(str(a) + str(b))
    num2 = 2 * a * b
    answer = max(num1, num2)
    return answer