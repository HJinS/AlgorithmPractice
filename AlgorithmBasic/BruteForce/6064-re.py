from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())

    Y = x
    cnt = x % (M + 1)

    for k in range(N):
        if Y % N == 0:
            ty = N
        else:
            ty = Y % N
        if ty == y:
            break
        cnt += M
        Y = ty + M

    if cnt > lcm(M, N):
        print(-1)
    else:
        print(cnt)

