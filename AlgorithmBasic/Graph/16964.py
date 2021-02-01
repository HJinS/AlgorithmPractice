N = int(input())
edge = [[] for i in range(N)]
user_ans = []
ans = []
order = [0 for i in range(N)]
visited = [False for i in range(N)]
res = True

for i in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

user_ans = list(map(int, input().split()))

for i in range(len(user_ans)):
    order[user_ans[i]-1] = i

for i in range(N):
    edge[i].sort(key = lambda x : order[x])

def dfs(v):
    visited[v] = True
    ans.append(v)
    for adj_v in edge[v]:
        if not visited[adj_v]:
            dfs(adj_v)

dfs(0)

for i in range(N):
    if user_ans[i] - 1 != ans[i]:
        res = False

if res:
    print("1")
else:
    print("0")