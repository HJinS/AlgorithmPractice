N = int(input())
B = list(map(int, input().split()))

A = []

def check(A, B, x):
    B.remove(x)
    A.append(x)

    if not B:
        return True
    if x * 2 in B:
        return check(A, B, x*2)
    if x % 3 == 0 and x // 3 in B:
        return check(A, B, x//3)
    return False

for i in range(N):
    A = []
    res = check(A, B.copy(), B[i])
    if res:
        print(*A)
        break
