import sys

sys.setrecursionlimit(100000)


def solution(number: str, k):
    selected_num = len(number) - k
    ans = 0

    def rec(number, idx, res, cnt):
        nonlocal ans
        if cnt >= 2:
            ans = max(ans, int("".join(list(res))))
            return
        for i in range(idx, len(number)):
            res = res. + number[i]
            rec(number, i + 1, res, cnt + 1)
            res = res - number[i]

    rec(number, 0, "", 0)
    return str(ans)

solution("1924", 2)