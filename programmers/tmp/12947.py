def solution(x):
    
    sum = 0
    num = x
    while num > 0:
        remain = num % 10
        num //= 10
        sum += remain
    
    if x % sum == 0:
        return True
    else:
        return False