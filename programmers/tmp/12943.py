def solution(num):
    cnt = 0
    while cnt < 500 and num > 1:
        if num % 2 == 0:
            num //= 2
        elif num % 2 != 0:
            num *= 3
            num += 1
        cnt += 1
            
    if cnt >= 500:
        return -1
    else:
        return cnt