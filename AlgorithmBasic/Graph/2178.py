from queue import Queue
N, M = map(int, input().split())
maze = []

ver = [i for i in range(N * M)]
edge = [[] for i in range(N * M)]
visited = [-1 for i in range(N * M)]
res = 987654321



for i in range(N):
    maze.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        visited[i*M+j] = 0
        if i > 0 and maze[i-1][j] == 1:
            edge[i*M+j].append((i-1)*M+j)
        if i < N-1 and maze[i+1][j] == 1:
            edge[i*M+j].append((i+1)*M+j)
        if j > 0 and maze[i][j-1] == 1:
            edge[i*M+j].append(i*M+(j-1))
        if j < M-1 and maze[i][j+1] == 1:
            edge[i*M+j].append(i*M+(j+1))

def bfs(v):
    global res
    d = [98765432 for i in range(N * M)]
    Q = Queue()
    Q.put(v)
    visited[v] = 1
    cnt = 0
    d[v] = 1
    while Q.empty() == False:
        vertical = Q.get()
        cnt += 1
        if vertical == N*M-1:
            res = min(res, cnt)

        for i in range(len(edge[vertical])):
            adj_v = edge[vertical][i]
            if visited[adj_v] == 0:
                visited[adj_v] = True
                d[adj_v] = min(d[adj_v], d[vertical] + 1)
                Q.put(adj_v)
    res = min(res, d[N*M-1])
for i in range(N*M):
    if visited[i] == 0:
        bfs(i)

print(res)