from collections import deque
from sys import stdin
import sys

sys.setrecursionlimit(100000)

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

    for adj_v in edge[v]:
        if not visited[adj_v]:
            ans[adj_v] = v
            dfs(start, adj_v)

def bfs(start, v):
    Q = deque()
    Q.append(v)
    visited[v] = True

    while Q:
        e = Q.popleft()
        
        for adj_v in edge[e]:
            if not visited[adj_v]:
                ans[adj_v] = e
                visited[adj_v] = True
                Q.append(adj_v)

dfs(0, 0)

for i in range(1, N):
    print(ans[i] + 1, "\n", end='')
