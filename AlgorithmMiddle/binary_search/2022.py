import math
x, y, c = map(float, input().split())

def func(mid):
    h1 = (x*x - mid*mid) ** 0.5
    h2 = (y*y - mid*mid) ** 0.5
    return (h1 * h2) / (h1 + h2)


low = 0
high = min(x, y)
res = 0

while high - low > 0.000001:
    mid = (low + high) / 2

    if func(mid) >= c:
        res = mid
        low = mid
    else:
        high = mid

print(res)