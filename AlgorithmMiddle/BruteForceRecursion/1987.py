from collections import deque
R, C = map(int, input().split())
board = []
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
used = [False for i in range(26)]
res = 0
for i in range(R):
    board.append(list(input()))

def DFS(x, y, cnt):
    global res, R, C
    used[ord(board[y][x]) - ord('A')] = True
    res = max(res, cnt)
    for i in range(4):
        nx = x + dir_x[i]
        ny = y + dir_y[i]
        if nx >= 0 and nx < C and ny >= 0 and ny < R and not used[ord(board[ny][nx]) - ord('A')]:
            used[ord(board[ny][nx]) - ord('A')] = True
            DFS(nx, ny, cnt+1)
            used[ord(board[ny][nx]) - ord('A')] = False

DFS(0,0,1)
print(res)