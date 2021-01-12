from math import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)

T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())
    
    Y = x
    cnt = x % (M+1)

    for i in range(N):
        ty = Y % N
        if ty == 0:
            ty = N
        if ty == y:
            break
        
        Y = ty + M
        cnt += M
    if cnt > lcm(M, N):
        print(-1)
    else:
        print(cnt)