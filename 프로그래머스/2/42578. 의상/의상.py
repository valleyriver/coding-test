from collections import Counter


def solution(clothes):
    answer = 1
    counter = {}
    
    for cloth in clothes:
        category = cloth[1]
        if category in counter:
            counter[category] += 1
        else:
            counter[category] = 1
            
    for count in counter.values():
        answer *= count + 1
        
    answer -= 1
    return answer