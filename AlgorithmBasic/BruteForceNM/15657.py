N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

res = [0 for i in range(M)]

def func(cnt):
    if cnt == M:
        for i in range(M):
            print(res[i], end=' ')
        print()
        return
    for i in range(N):
        if arr[i] >= res[cnt-1] or cnt == 0:
            res[cnt] = arr[i]
            func(cnt + 1)
            
func(0)