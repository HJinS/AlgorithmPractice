from collections import deque
from sys import stdin

N = int(stdin.readline())

edge = [[] for i in range(N)]
visited = [False for i in range(N)]
par = [-1 for i in range(N)]
ans = [-1 for i in range(N)]

for i in range(N-1):
    a, b = map(int, stdin.readline().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

def dfs(start, v):
    visited[v] = True
    if v == 0:
        tmp = v
        while par[tmp] != start:
            tmp1 = tmp
            tmp = par[tmp]
            ans[tmp] = tmp1
        ans[start] = tmp
        return

    for adj_v in edge[v]:
        if not visited[adj_v]:
            par[adj_v] = v
            dfs(start, adj_v)

def bfs(start, v):
    Q = deque()
    Q.append(v)
    visited[v] = True

    while Q:
        e = Q.popleft()
        if e == 0:
            tmp = e
            while par[tmp] != start:
                tmp1 = tmp
                tmp = par[tmp]
                ans[tmp] = tmp1
            ans[start] = tmp
            return
        
        for adj_v in edge[e]:
            if not visited[adj_v]:
                par[adj_v] = e
                visited[adj_v] = True
                Q.append(adj_v)

for i in range(N-1, 0, -1):
    visited = [False for j in range(N)]
    par = [-1 for j in range(N)]
    if ans[i] == -1:
        bfs(i, i)

for i in range(1, N):
    print(ans[i] + 1)
