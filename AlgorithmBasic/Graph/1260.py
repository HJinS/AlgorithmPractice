from queue import Queue

N, M, V = map(int, input().split())
ver = [i for i in range(N)]
edge = [[] for i in range(N)]

visited = [False for i in range(N)]

start = V-1

for i in range(M):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

for i in range(N):
    edge[i].sort()

def DFS(v):
    print(v+1,end=' ')
    visited[v] = True
    for i in range(len(edge[v])):
        op_ver = edge[v][i]
        if visited[op_ver] == False:
            DFS(op_ver)

def BFS(v):
    q = Queue()
    q.put(v)
    visited[v] = True
    while q.empty() == False:
        op_ver = q.get()
        print(op_ver+1,end=' ')
        
        for i in range(len(edge[op_ver])):
            tmp = edge[op_ver][i]
            if visited[tmp] == False:
                q.put(tmp)
                visited[tmp] = True

DFS(V-1)
print()
visited = [False for i in range(N)]
BFS(V-1)