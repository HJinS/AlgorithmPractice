from collections import deque

N, M = map(int, input().split())
board = []
visited = [[[[False for i in range(M)] for j in range(N)] for k in range(M)] for l in range(N)]
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
res = 987654321

for i in range(N):
    board.append(list(input()))

def move(x, y, dir_idx):
    cnt = 0
    dx = dir_x[dir_idx]
    dy = dir_y[dir_idx]
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def BFS():
    global res
    Q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                tmp_R = [j, i]
            if board[i][j] == 'B':
                tmp_B = [j, i]
    
    Q.append([tmp_R[0], tmp_R[1], tmp_B[0], tmp_B[1], 1])
    visited[tmp_R[1]][tmp_R[0]][tmp_B[1]][tmp_B[0]]

    while Q:
        red_x, red_y, blue_x, blue_y, cnt = Q.popleft()
        if cnt > 10:
            return
        for i in range(4):
            red_x_n, red_y_n, red_cnt = move(red_x, red_y, i)
            blue_x_n, blue_y_n, blue_cnt = move(blue_x, blue_y, i)

            if board[blue_y_n][blue_x_n] != 'O':
                if board[red_y_n][red_x_n] == 'O':
                    res = min(res, cnt)
                if red_x_n == blue_x_n and red_y_n == blue_y_n:
                    if red_cnt > blue_cnt:
                        red_x_n -= dir_x[i]
                        red_y_n -= dir_y[i]
                    else:
                        blue_x_n -= dir_x[i]
                        blue_y_n -= dir_y[i]
                if not visited[red_y_n][red_x_n][blue_y_n][blue_x_n]:
                    visited[red_y_n][red_x_n][blue_y_n][blue_x_n] = True
                    Q.append([red_x_n, red_y_n, blue_x_n, blue_y_n, cnt + 1])

BFS()

if res > 10:
    res = -1
print(res)