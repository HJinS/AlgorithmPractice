from collections import deque
N = int(input())
board = []
dir_x = [0, -1, 0, 1]
dir_y = [-1, 0, 1, 0]
shark_size = 2
eat_cnt = 0
visited = [[False for i in range(N)] for j in range(N)]

for i in range(N):
    board.append(list(map(int, input().split())))

def BFS():
    global shark_size, eat_cnt
    Q = deque()
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                Q.append([j, i])
                visited[i][j] = True
    cnt = 0
    while Q:
        for j in range(len(Q)):
            x, y = Q.popleft()
            for i in range(4):
                n_x = x + dir_x[i]
                n_y = y + dir_y[i]
                print("n_x = ", n_x, "n_y = ", n_y)
                if 0 <= n_x < N and 0 <= n_y < N:
                    if board[n_y][n_x] != 0 and board[n_y][n_x] != 9:
                        print("board = ", board[n_y][n_x])
                        if not visited[n_y][n_x]:
                            if shark_size > board[n_y][n_x]:
                                visited[n_y][n_x] = True
                                Q.append([n_x, n_y])
                                board[n_y][n_x] = 0
                                eat_cnt += 1
                                if eat_cnt == shark_size:
                                    shark_size += 1
                                break
                            elif shark_size == board[n_y][n_x]:
                                Q.append([n_x, n_y])
                                break
                    elif board[n_y][n_x] == 0 or board[n_y][n_x] == 9:
                        if not visited[n_y][n_x]:
                            visited[n_y][n_x] = True
                            Q.append([n_x, n_y])
        cnt += 1
    return cnt

res = BFS()
if eat_cnt == 0:
    print(0)
else:
    print(res)

