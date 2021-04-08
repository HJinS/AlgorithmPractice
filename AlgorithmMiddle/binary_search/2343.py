N, M = map(int, input().split())
arr = list(map(int, input().split()))

l, r = max(arr), sum(arr)
            
while l <= r:
    mid = (l + r) // 2
    blue_sum = 0
    blue_cnt = 0
    for i in range(N):
        blue_sum += arr[i]
        if blue_sum > mid:
            blue_sum = arr[i]
            blue_cnt += 1
        
    if blue_sum != 0:
        blue_cnt += 1

    if blue_cnt > M:
        l = mid+1
    else:
        r = mid-1

print(l)            