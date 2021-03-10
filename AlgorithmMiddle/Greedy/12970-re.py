N, K = map(int, input().split())
res = ['B' for i in range(N)]
a, b = 0, N

while a < N and a * b < K:
    a += 1
    b -= 1
if a == N:
    print(-1)
else:
    for i in range(a-1):
        res[i] = 'A'
    res[N-1] = 'A'
    dif = K - int((a-1) * b)
    tmp = res[N-dif-1]
    res[N-dif-1] = res[N-1]
    res[N-1] = tmp
    print("".join(res))
