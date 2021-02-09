import sys

sys.setrecursionlimit(100000)

N = int(input())
edge = [[] for i in range(N)]
visited = [False for i in range(N)]
par = [-1 for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

def dfs(v):
    visited[v] = True

    for adj_v in edge[v]:
        if not visited[adj_v]:
            par[adj_v] = v
            dfs(adj_v)

dfs(0)

for i in range(1, N):
    print(par[i] + 1)