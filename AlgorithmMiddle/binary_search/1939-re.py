from collections import deque
N, M = map(int, input().split())

island = [[] for i in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    island[a].append([b, c])
    island[b].append([a, c])

factory1, factory2 = map(int, input().split())

def BFS(weight):
    Q = deque()
    visited[factory1] = 1
    Q.append(factory1)

    while Q:
        start = Q.popleft()
        if start == factory2:
            return True
        for n_x, n_w in island[start]:
            if visited[n_x] == 0 and weight <= n_w:
                Q.append(n_x)
                visited[n_x] = 1
    return False

start, end = 1, 1000000000
while start <= end:
    visited = [False for i in range(N+1)]
    mid = (start + end) // 2
    if BFS(mid):
        start = mid + 1
    else:
        end = mid - 1
print(end)