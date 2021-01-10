from math import gcd
T = int(input())

def lcm(x, y):
    return x * y // gcd(x,y)

for i in range(T):
    M, N, x, y = map(int, input().split())
    cnt = x % (M + 1)
    Y = x
    for i in range(N):
        if Y % N == 0:
            ty = N
        else:
            ty = Y % N
        if ty == y:
            break
        Y = ty + M
        cnt += M
    if cnt > lcm(M, N):
        print(-1)
    else:
        print(cnt)
    