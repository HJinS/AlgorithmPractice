from collections import deque
N = int(input())
x_s, y_s, x_d, y_d = map(int, input().split())
dir_x = [-2, -2, 0, 0, 2, 2]
dir_y = [-1, 1, -2, 2, -1, 1]
visited = [[False for i in range(N)] for j in range(N)]
res = 987654321

def BFS():
    global x_s, y_s, x_d, y_d, res
    Q = deque()
    Q.append([x_s, y_s, 0])
    visited[y_s][x_s] = True

    while Q:
        x, y, cnt = Q.popleft()
        if x == x_d and y == y_d:
            res = min(res, cnt)
        for i in range(6):
            n_x = x + dir_x[i]
            n_y = y + dir_y[i]
            if n_x >= 0 and n_x < N and n_y >= 0 and n_y < N and not visited[n_y][n_x]:
                visited[n_y][n_x] = True
                Q.append([n_x, n_y, cnt+1])

BFS()

if res == 987654321:
    res = -1

print(res)