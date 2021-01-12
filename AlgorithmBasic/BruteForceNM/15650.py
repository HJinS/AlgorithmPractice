N, M = map(int, input().split())

visited = [False for i in range(N+1)]
arr = [-1 for i in range(M)]

def func(cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return
    for i in range(1, N+1):
        if visited[i] == False and (arr[cnt-1] < i or cnt == 0):
            visited[i] = True
            arr[cnt] = i
            func(cnt + 1)
            visited[i] = False

func(0)
            
        