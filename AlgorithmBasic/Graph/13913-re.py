from collections import deque

N, K = map(int, input().split())
visited = [False for i in range(100001)]
next_dir = [1, -1, 2]
parent = [0 for i in range(100001)]
path = []
res = 0
def BFS(start, des):
    Q = deque()
    Q.append(start)
    cnt = 0
    while Q:
        for i in range(len(Q)):
            e = Q.popleft()

            if e == des:
                tmp = e
                while tmp != start:
                    path.append(tmp)
                    tmp = parent[tmp]
                path.append(tmp)
                return cnt

            for i in range(3):
                if next_dir[i] == 2:
                    next_e = e * next_dir[i]
                else:
                    next_e = e + next_dir[i]
                
                if next_e >= 0 and next_e <= 100000 and not visited[next_e]:
                    visited[next_e] = True
                    Q.append(next_e)
                    parent[next_e] = e
        cnt += 1

res = BFS(N, K)

print(res)

for i in range(len(path)-1, -1, -1):
    print(path[i], end= ' ')