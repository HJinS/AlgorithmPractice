N, S = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

s, e, SUM = 0, 0, 0
min_length = N+1

pre_sum = [0 for _ in range(N+1)]

for i in range(1, N+1):
    pre_sum[i] = arr[i-1] + pre_sum[i-1]

while s < N:

    if pre_sum[e] - pre_sum[s] >= S:
        min_length = min(min_length, e-s)
        s += 1
    else:
        if e < N:
            e += 1
        else:
            s += 1

if min_length == N+1:
    min_length = 0
print(min_length)
