N, M, V = map(int, input().split())

ver = [i for i in range(N)]
edge = [[] for i in range(N)]
visited = [False for i in range(N)]
L = list()



for i in range(M):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

def dfs(v):
    print(v+1, end=' ')
    visited[v] = True
    for i in range(len(edge[v])):
        adj_ver = edge[v][i]
        if visited[adj_ver] == False:
            dfs(adj_ver)

def bfs(v):
    L.append(v)
    visited[v] = True
    while len(L) != 0:
        v = L[0]
        L.pop(0)
        print(v+1, end = ' ')
        for i in range(len(edge[v])):
            adj_v = edge[v][i]
            if visited[adj_v] == False:
                L.append(adj_v)
                visited[adj_v] = True

for i in range(N):
    edge[i].sort()

dfs(V-1)

for i in range(len(visited)):
    visited[i] =False

print()
bfs(V-1)
                