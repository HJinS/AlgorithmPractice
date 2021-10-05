def solution(n):
    ans = 0
    mul = 1
    
    while n > 0:
        re = n % 3
        n //= 3
        
        if re == 0:
            ans = ans + 4 * mul
            n -= 1
        elif re == 1:
            ans = ans + 1 * mul
        else:
            ans = ans + 2 * mul
        mul *= 10
        
    return str(ans)