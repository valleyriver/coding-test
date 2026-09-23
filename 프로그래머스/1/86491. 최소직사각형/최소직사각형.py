def solution(sizes):
    long_sides = []
    short_sides = []
    for w, h in sizes:
        if w > h:
            long_sides.append(w)
            short_sides.append(h)
        else:
            long_sides.append(h)
            short_sides.append(w)
    answer = max(long_sides) * max(short_sides)
    return answer