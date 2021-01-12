N, M = map(int, input().split())
arr = [-1 for i in range(M)]

def func(cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i],end=' ')
        print()
        return
    for i in range(1, N+1):
        arr[cnt] = i
        func(cnt + 1)

func(0)