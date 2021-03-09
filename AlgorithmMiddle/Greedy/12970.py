N, K = map(int, input().split())
res = ['B' for i in range(N)]
a, b = 0, N

while a * b < K and a < N:
    a += 1
    b -= 1
if a == N:
    print(-1)
else:
    for i in range(a-1):
        res[i] = 'A'
    res[N-1] = 'A'
    remain = K - int((a-1) * b)
    tmp = res[N-remain-1]
    res[N-remain-1] = res[N-1]
    res[N-1] = tmp
    print("".join(res))