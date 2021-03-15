N = int(input())
cards = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))
res = [-1 for i in range(M)]

def upper(find_num):
    l, r = 0, N-1
    while l < r:
        mid = int((l+r) // 2)
        if cards[mid] > find_num:
            r = mid
        else:
            l = mid + 1
    return r
def lower(find_num):
    l, r = 0, N-1
    while l < r:
        mid = int((l+r) // 2)

        if cards[mid] >= find_num:
            r = mid
        else:
            l = mid + 1
    return r
cards.sort()
for i in range(M):
    low = lower(num[i])
    up = upper(num[i])
    if up == N-1 and num[i] == cards[N-1]:
        up += 1
    print(up-low, end=' ')