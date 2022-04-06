def solution(x, n):
    cnt = 0
    arr = []
    num = 0
    while cnt < n:
        num += x
        arr.append(num)
        cnt += 1
    return arr