import sys
sys.setrecursionlimit(10000)
N = int(input())

Rom = [1, 5, 10, 50]
visited = [False for i in range(1001)]
res = 0

def DFS(cnt, d, total):
    global res
    if cnt == N:
        if not visited[total]:
            visited[total] = True
            res += 1
        return
    for i in range(d, 4):
        DFS(cnt + 1, i, total + Rom[i])

DFS(0, 0, 0)
print(res)