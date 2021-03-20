import sys
sys.setrecursionlimit(10000)

N, R, C = map(int, input().split())
count = 0
res = 0

while N > 0:
    tmp = (2**N) // 2
    if N > 1:
        if tmp > R and tmp <= C:
            count += tmp ** 2
            C -= tmp
        elif tmp <= R and tmp > C:
            count += (tmp**2) * 2
            R -= tmp
        elif tmp <= R and tmp <= C:
            count += (tmp**2) * 3
            R -= tmp
            C -= tmp
    elif N == 1:
        if R == 0 and C == 1:
            count += 1
        elif R == 1 and C == 0:
            count += 2
        elif R == 1 and C == 1:
            count += 3
    N -= 1
print(count)
