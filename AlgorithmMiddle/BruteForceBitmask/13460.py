from collections import deque
N, M = map(int, input().split())
board = []
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
visited = [[[[False for i in range(M)] for j in range(N)] for k in range(M)] for l in range(N)]
res = 987654321
r_cnt = 987654321
flag = False
for i in range(N):
    board.append(list(input()))

def printBoard():
    print()
    for i in range(N):
        for j in range(M):
            print(board[i][j], end='')
        print()
    print()

def BFS():
    global res, r_cnt, flag
    Q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                tmp_R = [j, i]
            if board[i][j] == 'B':
                tmp_B = [j, i]
    Q.append([tmp_R[0], tmp_R[1], tmp_B[0], tmp_B[1], -1, 0])
    visited[tmp_R[1]][tmp_R[0]][tmp_B[1]][tmp_B[0]] = True
    while Q:
        e = Q.popleft()
        red_x, red_y, blue_x, blue_y, state, cnt = map(int, e)

        if not flag and board[red_y][red_x] == 'O' and board[blue_y][blue_x] != 'O':
            print("r_cnt = ", r_cnt)
            flag = True
            r_cnt = min(r_cnt, cnt)
            res = min(res, cnt)
        if board[blue_y][blue_x] != 'O' and r_cnt == cnt:
            print("cnt = ", cnt)
            res = min(res, -1)
        for i in range(4):
            red_x_n = red_x + dir_x[i]
            red_y_n = red_y + dir_y[i]
            blue_x_n = blue_x + dir_x[i]
            blue_y_n = blue_y + dir_y[i]

            if red_x_n >= 0 and red_x_n < M and red_y_n >= 0 and red_y_n < N and blue_x_n >= 0 and blue_x_n < M and blue_y_n >= 0 and blue_y_n < N:
                if board[blue_y_n][blue_x_n] != '#' and board[red_y_n][red_x_n] != '#' and (red_x_n != blue_x_n or red_y_n != blue_y_n):
                    if not visited[red_y_n][red_x_n][blue_y_n][blue_x_n]:
                        if i != state:
                            Q.append([red_x_n, red_y_n, blue_x_n, blue_y_n, i, cnt+1])
                        else:
                            Q.append([red_x_n, red_y_n, blue_x_n, blue_y_n, i, cnt])
                        visited[red_y_n][red_x_n][blue_y_n][blue_x_n] = True
                elif board[blue_y_n][blue_x_n] == '#' and board[red_y_n][red_x_n] != '#' and (red_x_n != blue_x or red_y_n != blue_y):
                    if not visited[red_y_n][red_x_n][blue_y][blue_x]:
                        if i != state:
                            Q.append([red_x_n, red_y_n, blue_x, blue_y, i, cnt+1])
                        else:
                            Q.append([red_x_n, red_y_n, blue_x, blue_y, i, cnt])
                        visited[red_y_n][red_x_n][blue_y][blue_x] = True
BFS()
if res > 10:
    res = -1
print(res)