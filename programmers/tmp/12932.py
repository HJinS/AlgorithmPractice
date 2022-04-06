def solution(n):
    ans = []
    while n > 0:
        remain = n % 10
        ans.append(remain)
        n = n // 10
    return ans
    