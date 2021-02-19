import copy
n = int(input())
board = []
res = 0
for i in range(n):
    board.append(list(map(int, input().split())))

def move(dir):
    if dir == 0:
        for j in range(n):
            index = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[index][j] == 0:
                        board[index][j] = tmp
                    elif board[index][j] == tmp:
                        board[index][j] *= 2
                        index += 1
                    else:
                        index += 1
                        board[index][j] = tmp
    if dir == 1:
        for j in range(n):
            index = n-1
            for i in range(n-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[index][j] == 0:
                        board[index][j] = tmp
                    elif board[index][j] == tmp:
                        board[index][j] *= 2
                        index -= 1
                    else:
                        index -= 1
                        board[index][j] = tmp
    if dir == 2:
        for i in range(n):
            index = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][index] == 0:
                        board[i][index] = tmp
                    elif board[i][index] == tmp:
                        board[i][index] *= 2
                        index += 1
                    else:
                        index += 1
                        board[i][index] = tmp
    if dir == 3:
        for i in range(n):
            index = n-1
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][index] == 0:
                        board[i][index] = tmp
                    elif board[i][index] == tmp:
                        board[i][index] *= 2
                        index -= 1
                    else:
                        index -= 1
                        board[i][index] = tmp

def DFS(cnt):
    global res, board
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                res = max(res, board[i][j])
        return

    board_tmp = copy.deepcopy(board)    
    for i in range(4):
        move(i)
        DFS(cnt + 1)
        board = copy.deepcopy(board_tmp)

DFS(0)
print(res)