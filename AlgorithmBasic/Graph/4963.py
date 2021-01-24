import sys

sys.setrecursionlimit(15000)

ver = []
visited = []
edge = []
res = 0
mapList = []

def dfs(v):
    visited[v] =  1
    for i in range(len(edge[v])):
        adj_v = edge[v][i]
        if visited[adj_v] == 0:
            dfs(adj_v)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mapList = []
    edge = [[] for i in range(w*h)]
    ver = [i for i in range(w*h)]
    visited = [-1 for i in range(w*h)]

    for i in range(h):
        mapList.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if mapList[i][j] == 1:
                visited[i*w+j] = 0
                if i > 0 and mapList[i-1][j] == 1:
                    edge[i*w+j].append((i-1) * w + j)   
                if i < h-1 and mapList[i+1][j] == 1:
                    edge[i*w+j].append((i+1) * w + j)
                if j > 0 and mapList[i][j-1] == 1:
                    edge[i*w+j].append(i * w + (j-1))
                if j < w-1 and mapList[i][j+1] == 1:
                    edge[i*w+j].append(i * w + (j+1))
                
                if i < h-1 and j < w-1 and mapList[i+1][j+1] == 1:
                    edge[i*w+j].append((i+1) * w + (j+1))
                if i > 0 and j > 0 and mapList[i-1][j-1] == 1:
                    edge[i*w+j].append((i-1) * w + (j-1))
                if i < h-1 and j > 0 and mapList[i+1][j-1] == 1:
                    edge[i*w+j].append((i+1) * w + (j-1))
                if i > 0 and j < w-1 and mapList[i-1][j+1] == 1:
                    edge[i*w+j].append((i-1) * w + (j+1))

    res = 0
    for i in range(len(visited)):
        if visited[i] == 0:
            dfs(i)
            res += 1
    
    print(res)
