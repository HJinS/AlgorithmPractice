from collections import deque
N, K = map(int, input().split())
visited = [False for i in range(100001)]
direction = [1, -1, 2]
ans = []
res = 0
parent = [0 for i in range(100001)]
path = []

def BFS(start, des):
    Q = deque()
    Q.append(start)
    cnt = 0
    visited[start] = True
    while Q:
        for i in range(len(Q)):
            e = Q.popleft()
            ans.append(e)
            if e == des:
                tmp = e
                while tmp != start:
                    path.append(tmp)
                    tmp = parent[tmp]
                path.append(tmp)
                return cnt

            for j in range(3):
                if direction[j] == 2:
                    next_e = e * direction[j]
                else:
                    next_e = e + direction[j]
                if next_e >= 0 and next_e <= 100000 and not visited[next_e]:
                    Q.append(next_e)
                    visited[next_e] = True
                    parent[next_e] = e
        cnt += 1
res = BFS(N, K)
print(res)

for i in range(len(path)-1,-1,-1):
    print(path[i],end=' ')