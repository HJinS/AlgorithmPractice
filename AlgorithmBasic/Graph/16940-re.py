from collections import deque

N = int(input())
edge = [[] for i in range(N)]
visited = [False for i in range(N)]

user_ans = []
order = [0 for i in range(N)]
ans = []

for i in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

user_ans = list(map(int, input().split()))

for i in range(len(user_ans)):
    order[user_ans[i]-1] = i

for i in range(N):
    edge[i].sort(key=lambda x : order[x])

def BFS(v):
    Q = deque()
    Q.append(v)
    visited[v] = True

    while Q:
        e = Q.popleft()
        ans.append(e+1)
        for adj_v in edge[e]:
            if not visited[adj_v]:
                Q.append(adj_v)
                visited[adj_v] = True

BFS(0)

if ans == user_ans:
    print("1")
else:
    print("0")

                