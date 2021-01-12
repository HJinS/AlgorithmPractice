N, M = map(int, input().split())
arr = list(map(int, input().split()))

res = [0 for i in range(M)]

arr.sort()

def func(cnt):
    if cnt == M:
        for i in range(M):
            print(res[i], end=' ')
        print()
        return
    for i in range(N):
        res[cnt] = arr[i]
        func(cnt + 1)
func(0)