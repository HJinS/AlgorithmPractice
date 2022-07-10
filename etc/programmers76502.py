from collections import deque


def solution(s):
    # 단순히 브루트포스하게 다 확인하는 방법
    # 안될줄 알고 다른 방법 찾았는데 되더라
    cnt = 0
    i = 0

    def check(s):
        Q = deque()
        match = {
            '[': ']', '{': '}', '(': ')'
        }
        for c in s:
            if c == '(' or c == '{' or c == '[':
                Q.append(c)
            else:
                if not Q:
                    return False
                l = Q.pop()
                if match[l] != c:
                    return False
        if not Q:
            return True

    s = deque(s)
    res = 0
    for i in range(len(s)):
        s.rotate(-1)
        if check(s):
            res += 1
    return res








