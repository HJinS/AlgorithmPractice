def solution(n):
    
    num_list = []
    while n > 0:
        remain = n % 10
        n //= 10
        num_list.append(remain)
    num_list.sort(reverse=True)
    
    num = 0
    mul = 1
    
    for i in range(len(num_list)-1, -1, -1):
        num += mul * num_list[i]
        mul *= 10
    return num