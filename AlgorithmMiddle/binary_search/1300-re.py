N = int(input())
K = int(input())

def check(num):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(num // i, N)
    return cnt

l, r = 1, N*N
res = 0
while l <= r:
    mid = (l + r) // 2
    if check(mid) >= K:
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)