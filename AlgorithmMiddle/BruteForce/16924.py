N, M = map(int, input().split())

board = []
visited = [[0 for i in range(M)] for j in range(N)]
ans = []
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

for i in range(N):
    board.append(input())

def checks(x, y):
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
            checks(j, i)

res = 0
for i in range(N):
    for j in range(M):
        res += visited[i][j]

if res == 0:
    print(len(ans))
    for _ in ans:
        print(*_)
else:
    print(-1)