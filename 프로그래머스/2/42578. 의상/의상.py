from collections import Counter


def solution(clothes):
    answer = 1
    categories = []
    
    for cloth in clothes:
        categories.append(cloth[1])
    counter = Counter(categories)
    counts = list(counter.values())
    
    for count in counts:
        answer *= count + 1
        
    answer -= 1
    return answer