N, M = map(int, input().split())

arr = list(map(int, input().split()))

l, r = 0, max(arr)
res = r

while l <= r:
    mid = (l + r) // 2
    
    cnt = 1
    minV = arr[0]
    maxV = arr[0]
    for i in range(N):
        if arr[i] < minV:
            minV = arr[i]
        if arr[i] > maxV:
            maxV = arr[i]
        
        if (maxV - minV) > mid:
            cnt += 1
            minV = arr[i]
            maxV = arr[i]
    if cnt <= M:
        res = min(res, mid)
        r = mid - 1
    else:
        l = mid + 1
print(res)