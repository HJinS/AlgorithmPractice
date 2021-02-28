from collections import deque
N = int(input())
colors = []
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
visited = [[False for i in range(N)] for j in range(N)]

for i in range(N):
    colors.append(list(input()))

def BFS(color_week, start, color):
    Q = deque()
    Q.append([start[0], start[1]])
    visited[start[1]][start[0]] = True

    while Q:
        x, y = Q.popleft()
        if not color_week:
            for i in range(4):
                n_x = x + dir_x[i]
                n_y = y + dir_y[i]
                if 0 <= n_x < N and 0 <= n_y < N:
                    if not visited[n_y][n_x] and colors[n_y][n_x] == color:
                        visited[n_y][n_x] = True
                        Q.append([n_x, n_y])
        else:
            for i in range(4):
                n_x = x + dir_x[i]
                n_y = y + dir_y[i]
                if 0 <= n_x < N and 0 <= n_y < N:
                    if not visited[n_y][n_x]:
                        if color == "R" or color == "G":
                            if colors[n_y][n_x] != "B":
                                visited[n_y][n_x] = True
                                Q.append([n_x, n_y])
                        elif color == "B":
                            if colors[n_y][n_x] == color:
                                visited[n_y][n_x] = True
                                Q.append([n_x, n_y])

week_F = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(False, [j, i], colors[i][j])
            week_F += 1

week_T = 0
visited = [[False for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(True, [j, i], colors[i][j])
            week_T += 1
print(week_F, week_T)