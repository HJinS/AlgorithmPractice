import math
N = int(input())

s = ['  *   ', ' * *  ', '***** ']

def solve(shift):
    c = len(s)
    for i in range(c):
        s.append(s[i] + s[i])
        s[i] = ("   " * shift + s[i] + "   " * shift)

k = int(math.log(int(N / 3), 2))
for i in range(k):
    solve(int(2 ** i))
for i in range(N):
    print(s[i])
