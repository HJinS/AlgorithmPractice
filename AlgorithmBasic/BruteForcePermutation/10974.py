N = int(input())

visited = [False for i in range(N+1)]
res = [0 for i in range(N)]

def func(cnt):
    if cnt == N:
        for i in range(N):
            print(res[i],end=' ')
        print()
    
    for i in range(1,N+1):
        if visited[i] == False:
            visited[i] = True
            res[cnt] = i
            func(cnt+1)
            visited[i] = False
func(0)