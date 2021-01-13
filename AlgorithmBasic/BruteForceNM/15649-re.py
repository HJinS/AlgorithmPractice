N, M = map(int, input().split())
visited = [False for i in range(N+1)]

res = [0 for i in range(M)]

def func(cnt):
    if cnt == M:
        for i in range(M):
            print(res[i], end=' ')
        print()
        return
    for i in range(1,N+1):
        if visited[i] == False:
            visited[i] = True
            res[cnt] = i
            func(cnt + 1)
            visited[i] = False

func(0)
            