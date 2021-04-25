N = int(input())
rom = [1, 5, 10, 50]
visited = [False for i in range(1001)]

res = 0
def DFS(cnt, idx, sum):
    global res
    if cnt == N:
        if not visited[sum]:
            visited[sum] = True
            res += 1
        return
    for i in range(idx, 4):
        DFS(cnt+1, i, sum+rom[i])
DFS(0, 0, 0)
print(res)