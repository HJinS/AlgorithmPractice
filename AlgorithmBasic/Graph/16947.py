from collections import deque
import sys

sys.setrecursionlimit(100000)

n = int(input())

edge = [[] for i in range(n)]
visited = [False for i in range(n)]
dis = [987654 for i in range(n)]
cycle = False
isCycle = [False for i in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

def dfs(start, v, cnt):
    global cycle
    if start == v and cnt >= 2:
        cycle = True
        return

    visited[v] = True

    for i in range(len(edge[v])):
        adj_v = edge[v][i]
        if not visited[adj_v]:
            dfs(start, adj_v, cnt + 1)
        elif adj_v == start and cnt >= 2:
            dfs(start, adj_v, cnt)
        if cycle:
            return


def bfs(v):
    global visited
    visited = [False for i in range(n)]
    Q = deque()
    Q.append([v,0])
    while Q:
        e = Q.popleft()
        ver = e[0]
        cnt = e[1]

        if isCycle[ver] == True:
            return cnt

        for i in range(len(edge[ver])):
            adj_v = edge[ver][i]
            if visited[adj_v] == False:
                visited[adj_v] = True
                Q.append([adj_v, cnt + 1])

for i in range(n):
    visited = [False for i in range(n)]
    cycle = False
    dfs(i, i, 0)
    if cycle:
        isCycle[i] = True

for i in range(n):
    if isCycle[i]:
        dis[i] = 0
    else:
        dis[i] = bfs(i)

for d in dis:
    print(d,end=' ')
