from collections import deque

T = int(input())
chess = [[]]
visited = [[]]
l = 0

dir_x = [1, 1, -1, -1, 2, 2, -2, -2]
dir_y = [2, -2, 2, -2, 1, -1, 1, -1]

Q = deque()

def bfs(now_x, now_y, des_x, des_y):
    Q.append([now_x,now_y])
    chess[now_y][now_x] = 0
    visited[now_y][now_x] = 1
    while Q:
        loc = Q.popleft()
        x = loc[0]
        y = loc[1]
        if x == des_x and y == des_y:
            break
        for i in range(8):
            nx = x + dir_x[i]
            ny = y + dir_y[i]
            if nx >= 0 and nx < l and ny >= 0 and ny < l and visited[ny][nx] == 0:
                Q.append([nx,ny])
                visited[ny][nx] = 1
                chess[ny][nx] = min(chess[ny][nx], chess[y][x] + 1)

for i in range(T):
    l = int(input())
    now_x, now_y = map(int, input().split())
    des_x, des_y = map(int, input().split())
    chess = [[987654321 for i in range(l)] for j in range(l)]
    visited = [[0 for i in range(l)] for j in range(l)]
    bfs(now_x,now_y,des_x,des_y)
    print(chess[des_y][des_x])
    Q.clear()