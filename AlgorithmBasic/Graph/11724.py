N, M = map(int, input().split())

ver = [i for i in range(N)]
edge = [[] for i in range(N)]
visited = [False for i in range(N)]
res = 0

for  i in range(M):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

def DFS(v):
    visited[v] = True
    for i in range(len(edge[v])):
        op_ver = edge[v][i]
        if visited[op_ver] == False:
            DFS(op_ver)

for i in range(N):
    if visited[i] == False:
        DFS(i)
        res += 1
print(res)