import sys
n = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()

s, e = 0, n-1
MIN = sys.maxsize
ans = arr[s], arr[e]

while s < e:
    sum = arr[s] + arr[e]
    if MIN > abs(sum):
        MIN = abs(sum)
        ans = arr[s], arr[e]
    if sum < 0:
        s += 1
    elif sum == 0:
        ans = arr[s], arr[e]
        break
    else:
        e -= 1

print(ans[0], ans[1])

