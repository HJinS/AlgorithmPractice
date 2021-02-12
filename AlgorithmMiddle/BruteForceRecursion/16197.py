from collections import deque
N, M = map(int, input().split())
board = []
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
res = 987654321
visited = [[[[False for i in range(M+2)] for j in range(N+2)] for k in range(M+2)] for l in range(N+2)]

for i in range(N):
    board.append(list(input()))

def BFS():
    global res, N, M
    Q = deque()

    tmp_x = -1
    tmp_y=  -1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                if tmp_x == -1 and tmp_y == -1:
                    tmp_x = j
                    tmp_y = i
                else:
                    Q.append([j, i, tmp_x, tmp_y, 0])
                    visited[i][j][tmp_y][tmp_x] = True

    while Q:
        e = Q.popleft()
        cur_x1 = e[0]
        cur_y1 = e[1]
        cur_x2 = e[2]
        cur_y2 = e[3]
        cnt = e[4]

        flag = False
        for i in range(4):
            new_x1 = cur_x1 + dir_x[i]
            new_y1 = cur_y1 + dir_y[i]
            new_x2 = cur_x2 + dir_x[i]
            new_y2 = cur_y2 + dir_y[i]

            if new_x1 >= 0 and new_x1 < M and new_y1 >= 0 and new_y1 < N and new_x2 >= 0 and new_x2 < M and new_y2 >= 0 and new_y2 < N:
                if not visited[new_y1][new_x1][new_y2][new_x2] and board[new_y1][new_x1] != '#' and board[new_y2][new_x2] == '#':
                    Q.append([new_x1, new_y1, cur_x2, cur_y2, cnt +1])
                    visited[new_y1][new_x1][new_y2][new_x2] = True
                    
                elif not visited[new_y1][new_x1][new_y2][new_x2] and board[new_y2][new_x2] != '#' and board[new_y1][new_x1] == '#':
                    Q.append([cur_x1, cur_y1, new_x2, new_y2, cnt +1])
                    visited[new_y1][new_x1][new_y2][new_x2] = True

                elif not visited[new_y1][new_x1][new_y2][new_x2] and board[new_y2][new_x2] != '#' and board[new_y1][new_x1] != '#':
                    Q.append([new_x1, new_y1, new_x2, new_y2, cnt +1])
                    visited[new_y1][new_x1][new_y2][new_x2] = True

            elif (not (new_x1 >= 0 and new_x1 < M and new_y1 >= 0 and new_y1 < N)) and (not (new_x2 >= 0 and new_x2 < M and new_y2 >= 0 and new_y2 < N)):
                continue
            else:
                res = min(res, cnt+1)
BFS()

if res > 10:
    res = -1

print(res)