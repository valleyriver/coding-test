def solution(s):
    st = []
    for i in range(len(s)):
        if s[i] == '(':
            st.append(s[i])
        else:
            if len(st) == 0:
                return False
            st.pop()
    if len(st) != 0:
        return False
    return True