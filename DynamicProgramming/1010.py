import operator as op
from functools import reduce

def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1,r+1), 1)
    return numerator // denominator

T = int(input())

for i in range(T):
    w, e = map(int, input().split())
    dp = [0 for i in range(e+1)]
    dp[w] = 1
    for j in range(w+1,e+1):
        dp[j] = dp[j-1] + nCr(j-1,w-1)
    print(dp[e])
