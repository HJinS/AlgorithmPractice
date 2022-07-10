import math


def solution(a):
    gcd
    for idx, num in enumerate(a):
        if idx == 0:
            gcd = num
        else:
            gcd = math.gcd(gcd, num)
        if gcd == 1:
            break

    return gcd * len(a)

