N = int(input())
K = int(input())

def check(mid):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid // i, N)
    return cnt

l, r = 1, N*N
res = 1

while l <= r:
    mid = (l + r) // 2
    if check(mid) >= K:
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)