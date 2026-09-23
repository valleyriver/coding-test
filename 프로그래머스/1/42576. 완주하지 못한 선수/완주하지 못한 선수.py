def solution(participant, completion):
    answer = ''
    st = {}
    for name in participant:
        if name in st:
            st[name] += 1
        else:
            st[name] = 1
    for name in completion:
        st[name] -= 1
    for name, count in st.items():
        if count == 1:
            answer = name
    return answer