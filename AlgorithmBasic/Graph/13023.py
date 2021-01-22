N, M = map(int ,input().split())

people = [i for i in range(N)]
relation = [[] for i in range(N)]

visited = [False for i in range(N)]
res = False

for i in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

def solve(index, cnt):
    global res
    if cnt == 4:
        res = True
        return
    
    visited[index] = True
    for i in range(len(relation[index])):
        n_index = relation[index][i]
        if visited[n_index] == False:
            solve(n_index, cnt + 1)
        if res:
            return
    visited[index] = False

for i in range(N):
    solve(i,0)
    if res:
        break
if res:
    print("1")
else:
    print("0")
