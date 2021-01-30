import sys

sys.setrecursionlimit(100000)

N, M = map(int, input().split())

board = []
visited = [[False for i in range(M)] for j in range(N)]

dir_x = [1,0,-1,0]
dir_y = [0,1,0,-1]
res = False

for i in range(N):
    board.append(list(map(str,input())))

def dfs(bx, by, x, y, color, cnt):
    global res

    if visited[y][x] == True:
        res = True
        return

    visited[y][x] = True
    for i in range(4):
        nx = x + dir_x[i]
        ny = y + dir_y[i]
        
        if bx != nx or by != ny:
            if nx >= 0 and nx < M and ny >= 0 and ny < N and board[ny][nx] == color:
                dfs(x, y, nx, ny, color, cnt+1)
            
for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            dfs(j, i, j, i, board[i][j], 0)

if res:
    print("Yes")
else:
    print("No")