N = int(input())
cards = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))
res = [-1 for i in range(M)]
cards.sort()

def upper(num):
    l, r = 0, N-1
    while l < r:
        mid = ((l + r) // 2)
        if cards[mid] > num:
            r = mid
        else:
            l = mid + 1
    return r

def lower(num):
    l, r = 0, N-1
    while l < r:
        mid = ((l + r) // 2)
        if cards[mid] >= num:
            r = mid
        else:
            l = mid + 1
    return r

for i in range(M):
    up = upper(num[i])
    low = lower(num[i])

    if up == N-1 and num[i] == cards[N-1]:
        up += 1
    print(up-low, end=' ')