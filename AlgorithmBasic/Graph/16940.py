from collections import deque
import sys

N = int(input())

edge = [[] for i in range(N)]
ans = []
real_ans = []
visited = [False for i in range(N)]
order = [0 for i in range(N)]
res = True

for i in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

ans = list(map(int, input().split()))

for i, e in enumerate(ans):
    order[e-1] = i

for i in range(N):
    edge[i].sort(key = lambda x : order[x])

def bfs(v):
    global res
    global real_ans
    Q = deque()
    Q.append(v)
    visited[v] = True
    while Q:
        ver = Q.popleft()
        real_ans.append(ver)
        for adj_v in edge[ver]:
            if not visited[adj_v]:
                Q.append(adj_v)
                visited[adj_v] = True

bfs(0)

for i in range(N):
    if ans[i]-1 != real_ans[i]:
        res = False

if res:
    print("1")
else:
    print("0")