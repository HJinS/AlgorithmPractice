from collections import deque
N, M, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
res = []

if N < M + K -1 or N > M * K:
    print(-1)
else:
    Q = deque()
    Q.append(0)
    Q.append(K)
    M -= 1
    N -= K

    left_clu = 1 if M == 0 else int(N // M)
    left_num = 0 if M == 0 else int(N % M)

    for i in range(M):
        Q.append(Q[len(Q)-1] + left_clu + (1 if left_num > 0 else 0))
        if left_num > 0:
            left_num -= 1
    for i in range(len(Q)-1):
        tmp = arr[Q[i]:Q[i+1]]
        tmp.reverse()
        for e in tmp:
            res.append(e)
    for e in res:
        print(e, end=' ')