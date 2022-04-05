def solution(n):
    arr = [True for i in range(n+1)]
    arr[0], arr[1] = False, False
    
    for i in range(2, n+1):
        if arr[i]:
            j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1
    
    cnt = 0

    for i in range(2, n+1):
        if arr[i]:
            cnt += 1
    return cnt