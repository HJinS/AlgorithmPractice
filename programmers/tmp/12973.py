from collections import deque
def solution(s):
    
    idx = 0
    length = len(s)
    Q = deque()
    while idx < length:
        if not Q:
            Q.append(s[idx])
            idx += 1
        else:
            if Q[-1] == s[idx]:
                Q.pop()
                idx += 1
            else:
                Q.append(s[idx])
                idx += 1
    if Q:
        return 0
    else:
        return 1
    