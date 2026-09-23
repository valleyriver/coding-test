def solution(nums):
    max_count = len(nums) // 2
    type_count = len(set(nums))
    answer = min(max_count, type_count)
    return answer