N, M = map(int, input().split())
arr = list(map(int, input().split()))

visitid = [False for i in range(N)]
res = [0 for i in range(M)]

arr.sort()

def func(cnt):
    if cnt == M:
        for i in range(M):
            print(res[i],end=' ')
        print()
        return
    for i in range(N):
        if visitid[i] == False and (arr[i] > res[cnt-1] or cnt == 0):
            visitid[i] = True
            res[cnt] = arr[i]
            func(cnt + 1)
            visitid[i] = False
func(0)