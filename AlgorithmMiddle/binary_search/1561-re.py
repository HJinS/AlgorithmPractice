N, M = map(int, input().split())
rides = list(map(int, input().split()))

def find():
    l, r = 0, 2000000000 * 30
    res = 0
    while l <= r:
        mid = (l + r) // 2
        children = M
        for i in range(M):
            children += mid // rides[i]
        
        if children >= N:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

time = find()
children = M
for i in range(M):
    children += (time-1) // rides[i]
res = 0
for i in range(M):
    if not time % rides[i]:
        children += 1
    if children == N:
        res = i+1
        break
print(res)