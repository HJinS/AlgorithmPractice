#백준 센세 대박
N = int(input())
B = list(map(int, input().split()))

A = []

for i in range(N):
    origin_num = B[i]
    cnt = 0
    while True:
        if B[i] % 3 == 0:
            B[i] //= 3
            cnt += 1
        else:
            break

    A.append([cnt, origin_num])

A.sort(key = lambda x: (-x[0], x[1]))

for i in range(N):
    print(A[i][1], end=' ')
