arr = list(map(int, input().split()))

prices = arr[:3]
X, Y = map(int, arr[3:])

Z = min(X, Y)

res = 0

if prices[0] + prices[1] > prices[2] * 2:
    res += prices[2] * 2 * Z
    X -= Z
    Y -= Z
    if Y != 0:
        res += min(prices[1] * Y, prices[2] * 2 * Y)
    elif X != 0:
        res += min(prices[0] * X, prices[2] * 2 * X)
else:
    res += prices[0] * X + prices[1] * Y

print(res)
