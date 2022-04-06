def solution(n):
    answer = 0
    while n > 0:
        remain = n % 10
        answer += remain
        n = n // 10
    return answer