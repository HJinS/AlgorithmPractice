from collections import deque
import sys

N, M = map(int, input().split())
s = [[] for i in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])

def BFS(mid):
    visited[factory1] = 1
    Q = deque()
    Q.append(factory1)

    while Q:
        start = Q.popleft()
        if start == factory2:
            return True   
        for n_x, n_c in s[start]:
            if visited[n_x] == 0 and mid <= n_c:
                Q.append(n_x)
                visited[n_x] = 1
    return False

factory1, factory2 = map(int, input().split())
low, high = 1, 1000000000

while low <= high:
    visited = [0 for i in range(N+1)]
    mid = (low + high) // 2
    if BFS(mid):
        low = mid + 1
    else:
        high = mid -1
print(high)