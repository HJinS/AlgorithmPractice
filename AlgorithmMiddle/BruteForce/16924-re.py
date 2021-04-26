N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(input()))
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
visited = [[0 for _ in range(M)] for __ in range(N)]
ans = list()

def check(x, y):
    global ans
    for s in range(1, M):
        flag = True
        for i in range(4):
            nx = x + dir_x[i] * s
            ny = y + dir_y[i] * s
            if not (0 <= nx < M and 0 <= ny < N and board[ny][nx] == '*'):
                flag = False
                break
        if not flag:
            break
        ans.append([y+1, x+1, s])
        for i in range(4):
            nx = x + dir_x[i] * s
            ny = y + dir_y[i] * s
            visited[ny][nx] = 0
        visited[y][x] = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == '*':
            visited[i][j] = 1

for i in range(N):
    for j in range(M):
        if board[i][j] == '*':
            check(j, i)

sum = 0
for i in range(N):
    for j in range(M):
        sum += visited[i][j]
    
if sum == 0:
    print(len(ans))
    for e in ans:
        print(*e)
else:
    print(-1)