from collections import Counter


def solution(nums):
    max_count = len(nums) // 2
    type_count = len(Counter(nums))
    answer = min(max_count, type_count)
    return answer