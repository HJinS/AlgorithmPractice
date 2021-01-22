T = int(input())
ver = []
edge = []
visited = []
v, e = 0, 0
res = True

def BFS(v):
    global res
    L = list()
    L.append(v)
    visited[v] = 1
    while len(L) != 0:
        op_v = L[0]
        L.pop(0)
        for i in range(len(edge[op_v])):
            adj_v = edge[op_v][i]
            if visited[adj_v] == 0:
                L.append(adj_v)
                visited[adj_v] = visited[op_v] * (-1)
            if visited[op_v] + visited[adj_v] != 0:
                res = False



for i in range(T):
    v, e = map(int, input().split())
    visited = [0 for i in range(v)]
    edge = [[] for i in range(v)]
    ver = [i for i in range(v)]
    res = True
    for i in range(e):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    for i in range(v):
        if visited[i] == 0:
            BFS(i)
    if res == False:
        print("NO")
    else:
        print("YES")
