import sys
sys.setrecursionlimit(10000000)

N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(0)
    exit()

def check(first, second, B):
    diff = second - first
    new = [first + diff * i for i in range(len(B))]
    flag = True
    change = 0
    for i in range(2, len(B)):
        if abs(new[i] - B[i]) > 1:
            return [False, change]
        if new[i] == B[i]:
            pass
        else:
            change += 1
    return [True, change]

res = 99999999
for k in [-1, 0, 1]:
    for u in [-1, 0, 1]:
        flag, change = check(B[0] + k, B[1] + u, B)
        if flag:
            if k != 0:
                change += 1
            if u != 0:
                change += 1
            res = min(res, change)

if res != 99999999:
    print(res)
else:
    print(-1)