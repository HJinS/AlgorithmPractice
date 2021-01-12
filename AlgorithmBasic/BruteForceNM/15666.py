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
    
    before = -1
    for i in range(N):
        if (i == 0 or before != arr[i]) and (arr[i] >= res[cnt-1] or cnt == 0):
            res[cnt] = arr[i]
            before = arr[i]
            func(cnt + 1)
    
func(0)