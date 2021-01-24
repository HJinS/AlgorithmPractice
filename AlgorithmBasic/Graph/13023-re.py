N, M = map(int, input().split())

ver = [i for i in range(N)]
edge = [[] for i in range(N)]
visited = [False for i in range(N)]
res = False

for i in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

def dfs(index, cnt):
    global res
    if cnt == 4:
        res = True
        return
    visited[index] = True
    for i in range(len(edge[index])):
        op_ver = edge[index][i]
        if visited[op_ver] == False:
            dfs(op_ver, cnt+1)
        if res == True:
            return
    visited[index] = False


for i in range(N):
    if visited[i] == False:
        dfs(i, 0)

if res == False:
    print('0')
else:
    print('1')