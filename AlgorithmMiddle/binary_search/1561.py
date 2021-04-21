N, M = map(int, input().split())
rides_time = list(map(int, input().split()))

def find():
    l, r = 0, 2000000000*30
    res = -1
    while l <= r:
        mid = (l + r) // 2
        children = M
        for i in range(M):
            children += mid // rides_time[i]
        
        if children >= N:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return res

if N <= M:
    print(N)
else:
    time = find()
    children = M
    for i in range(M):
        children += (time-1) // rides_time[i]

    
    for i in range(M):
        if not time % rides_time[i]:
            children += 1
        if children == N:
            print(i + 1)
            break