N, M = map(int, input().split())

number = [False for i in range(N+1)]
arr = [-1 for i in range(M)]

def func(cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i],end=' ')
        print()
        return
    for i in range(1, N+1):
        if number[i] == False:
            number[i] = True
            arr[cnt] = i
            func(cnt + 1)
            number[i] = False

func(0)
