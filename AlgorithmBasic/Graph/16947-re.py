from collections import deque
import sys

sys.setrecursionlimit(100000)

N = int(input())

edge = [[] for i in range(N)]
cir = False
is_circle = [False for i in range(N)]
visited = [False for i in range(N)]
dis = [987654321 for i in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)


def dfs(start, v, cnt):
    global cir
    if visited[v] and cnt >= 2:
        cir = True
        return

    visited[v] = True
    for ver in edge[v]:
        if not visited[ver]:
            dfs(start, ver, cnt+1)
        elif start == ver and cnt >= 2:
            dfs(start, ver, cnt)
        elif cir:
            return

def bfs(v):
    global visited
    visited = [False for i in range(N)]
    Q = deque()
    Q.append([v, 0])

    while Q:
        e = Q.popleft()
        ver = e[0]
        cnt = e[1]
        if is_circle[ver]:
            return cnt

        for adj_v in edge[ver]:
            if not visited[adj_v]:
                Q.append([adj_v, cnt+1])
                visited[adj_v] = True

for i in range(N):
    visited = [False for i in range(N)]
    cir = False
    dfs(i,i,0)
    if cir:
        is_circle[i] = True

for i in range(N):
    if is_circle[i]:
        dis[i] = 0
    else:
        dis[i] = bfs(i)

for i in range(N):
    print(dis[i], end = ' ')