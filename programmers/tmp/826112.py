def solution(price, money, count):
    
    total_cnt = 0
    
    for i in range(1, count+1):
        total_cnt += price * i
    
    if total_cnt > money:
        return total_cnt - money
    else:
        return 0