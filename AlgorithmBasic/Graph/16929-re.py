N, M = map(int, input().split())

dots = []
visited = [[False for i in range(M)] for j in range(N)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
res = False

for i in range(N):
    dots.append(list(map(str,input())))

def dfs(bx, by, x, y, color):
    global res
    if visited[y][x]:
        res = True
        return
    visited[y][x] = True

    for i in range(4):
        nx = x + dir_x[i]
        ny = y + dir_y[i]
        if nx >= 0 and nx < M and ny >= 0 and ny < N and dots[ny][nx] == color:
            if bx != nx or by != ny:
                dfs(x, y, nx, ny, color)

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(j, i, j, i, dots[i][j])

if res:
    print("Yes")
else:
    print("No")