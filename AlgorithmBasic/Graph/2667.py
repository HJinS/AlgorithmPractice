n = int(input())
house = []
ver = [i for i in range(n*n)]
edge = [[] for i in range(n*n)]
visited = [0 for i in range(n*n)]

res = []

for i in range(n):
    house.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if house[i][j] == 1:                
            if i > 0 and house[i-1][j] == 1:
                edge[j+i*n].append(j+(i-1)*n)

            if j > 0 and house[i][j-1] == 1:
                edge[j+i*n].append((j-1)+i*n)

            if i < n-1 and house[i+1][j] == 1:
                edge[j+i*n].append(j+(i+1)*n)

            if j < n-1 and house[i][j+1] == 1:
                edge[j+i*n].append((j+1)+i*n)
        else:
            visited[j+i*n] = -1

def dfs(v, cnt):
    visited[v] = 1
    cnt += 1
    for i in range(len(edge[v])):
        adj_v = edge[v][i]
        if visited[adj_v] == 0:
            cnt = dfs(adj_v, cnt)
    return cnt

for i in range(n*n):
    if visited[i] == 0:
        res.append(dfs(i,0))

res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])
