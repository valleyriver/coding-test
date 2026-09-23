def solution(sizes):
    max_long = 0
    max_short = 0
    for w, h in sizes:
        max_long = max(max_long, max(w, h))
        max_short = max(max_short, min(w, h))
    answer = max_long * max_short
    return answer