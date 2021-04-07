x, y, c = map(float, input().split())

def func(w):
    h1 = (x * x - w * w) ** 0.5
    h2 = (y * y - w * w) ** 0.5

    return (h1 * h2) / (h1 + h2)

h_min = 0
h_max = min(x, y)
res = 0
while h_max - h_min > 0.000001:
    mid = (h_min + h_max) / 2

    if func(mid) >= c:
        res = mid
        h_min = mid
    else:
        h_max = mid
    
print(res)