k = int(input())

ver = []
edge = [[]]
visited = []
res = True

def bfs(v):
    global res
    L = list()
    L.append(v)
    visited[v] = 1

    while len(L) != 0:
        vertex = L[0]
        L.pop(0)
        for i in range(len(edge[vertex])):
            adj_v = edge[vertex][i]
            if visited[adj_v] == 0:
                visited[adj_v] = visited[vertex] * (-1)
                L.append(adj_v)
            if visited[adj_v] + visited[vertex] != 0:
                res = False
                break

for i in range(k):
    V, E = map(int, input().split())
    ver = [i for i in range(V)]
    edge = [[] for i in range(V)]
    visited = [0 for i in range(V)]
    res = True

    for i in range(E):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    
    for i in range(V):
        edge[i].sort()

    for i in range(V):
        if visited[i] == 0:
            bfs(i)
    
    if res:
        print("YES")
    else:
        print("NO")