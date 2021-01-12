N, M = map(int ,input().split())
arr = list(map(int ,input().split()))

visited = [False for i in range(N)]

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
        if (cnt == 0 or arr[i] >= res[cnt-1]) and (i ==0 or before != arr[i]) and visited[i] == False:
            visited[i] = True
            before = arr[i]
            res[cnt] = arr[i]
            func(cnt + 1)
            visited[i] = False
func(0)