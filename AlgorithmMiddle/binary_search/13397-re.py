N, M = map(int, input().split())

arr = list(map(int, input().split()))

l, r = 0, max(arr)
res = r

while l <= r:
    mid = (l + r) // 2

    min_sub, max_sub = arr[0], arr[0]
    cnt = 1
    for i in range(N):
        min_sub = min(min_sub, arr[i])
        max_sub = max(max_sub, arr[i])

        if max_sub - min_sub > mid:
            cnt += 1
            max_sub = arr[i]
            min_sub = arr[i]
    
    if cnt <= M:
        res = min(res, mid)
        r = mid - 1
    else:
        l = mid + 1
print(res)