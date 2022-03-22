from collections import deque
import sys

def solution(board):
    answer = 0
    N, M = len(board), len(board[0])
    visited = deque()
    x1, y1, x2, y2 = 0, 0, 1, 0
    dir_x, dir_y = [0, 1, 0, -1, 0], [1, 0, -1, 0, 0]
    Q = deque()
    Q.append([x1, y1, x2, y2, 0])
    visited.append([x1, y1, x2, y2])
    res = sys.maxsize
    while Q:
        cur_x1, cur_y1, cur_x2, cur_y2, cnt = Q.popleft()
        print("curx1   cury1   cur_x2   cur_y2   cnt")
        print(cur_x1, "    ", cur_y1, "    ", cur_x2, "    ", cur_y2, "    ", cnt)
        if (cur_x1 == M-1 and cur_y1 == N-1) or (cur_x2 == M-1 and cur_y2 == N-1):
            res = min(res, cnt)
        
        ## 1, 2이면 핀 기준 시계
        ## 3, 4이면 핀 기준 반시게
        for i in range(0, 5):
            new_cnt = cnt
            rotated_flag = False
            if i == 0:
                rotated_x1, rotated_y1, rotated_x2, rotated_y2 = cur_x1, cur_y1, cur_x2, cur_y2
            else:
                if i % 2 == 0:
                    pinned_x, pinned_y = cur_x1, cur_y1
                    ano_x, ano_y = cur_x2, cur_y2
                    rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y, ano_x, ano_y
                    if pinned_x == ano_x:
                        # 시계
                        if i == 2:
                            if pinned_y > ano_y:
                                if 0 <= ano_x+1 < M and 0 <= pinned_x+1 < M:
                                    if board[ano_y][ano_x+1] == 0 and board[pinned_y][pinned_x+1] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y, pinned_x+1, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                            elif pinned_y < ano_y:
                                if 0 <= ano_x-1 < M and 0 <= pinned_x-1 < M:
                                    if board[ano_y][ano_x-1] == 0 and board[pinned_y][pinned_x-1] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y, pinned_x-1, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                        #반시계
                        elif i == 4:
                            if pinned_y > ano_y:
                                if 0 <= ano_x-1 < M and 0 <= pinned_x-1 < M:
                                    if board[ano_y][ano_x-1] == 0 and board[pinned_y][pinned_x-1] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y, pinned_x-1, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                            elif pinned_y < ano_y:
                                if 0 <= ano_x+1 < M and 0 <= pinned_x+1 < M:
                                    if board[ano_y][ano_x+1] == 0 and board[pinned_y][pinned_x+1] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y, pinned_x+1, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                    elif pinned_y == ano_y:
                        # 시계
                        if i == 2:
                            if pinned_x > ano_x:
                                if 0 <= ano_y-1 < N and 0 <= pinned_y-1 < N:
                                    if board[ano_y-1][ano_x] == 0 and board[pinned_y-1][pinned_x] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y, pinned_x, pinned_y-1
                                        new_cnt += 1
                                        rotated_flag = True
                            elif pinned_x < ano_x:
                                if 0 <= ano_y+1 < N and 0 <= pinned_y+1 < N:
                                    if board[ano_y+1][ano_x] == 0 and board[pinned_y+1][pinned_x] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y, pinned_x, pinned_y+1
                                        new_cnt += 1
                                        rotated_flag = True
                        #반시계
                        elif i == 4:
                            if pinned_x > ano_x:
                                if 0 <= ano_y+1 < N and 0 <= pinned_y+1 < N:
                                    if board[ano_y+1][ano_x] == 0 and board[pinned_y+1][pinned_x] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y, pinned_x, pinned_y+1
                                        new_cnt += 1
                                        rotated_flag = True
                            elif pinned_x < ano_x:
                                if 0 <= ano_y-1 < N and 0 <= pinned_y-1 < N:
                                    if board[ano_y-1][ano_x] == 0 and board[pinned_y-1][pinned_x] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y, pinned_x, pinned_y-1
                                        new_cnt += 1
                                        rotated_flag = True
                else:
                    pinned_x, pinned_y = cur_x2, cur_y2
                    ano_x, ano_y = cur_x1, cur_y1
                    rotated_x1, rotated_y1, rotated_x2, rotated_y2 = ano_x, ano_y, pinned_x, pinned_y
                    if pinned_x == ano_x:
                        # 시계
                        if i == 1:
                            if pinned_y > ano_y:
                                if 0 <= ano_x+1 < M and 0 <= pinned_x+1 < M:
                                    if board[ano_y][ano_x+1] == 0 and board[pinned_y][pinned_x+1] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x+1, pinned_y, pinned_x, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                            elif pinned_y < ano_y:
                                if 0 <= ano_x-1 < M and 0 <= pinned_x-1 < M:
                                    if board[ano_y][ano_x-1] == 0 and board[pinned_y][pinned_x-1] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x-1, pinned_y, pinned_x, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                        #반시계
                        elif i == 3:
                            if pinned_y > ano_y:
                                if 0 <= ano_x-1 < M and 0 <= pinned_x-1 < M:
                                    if board[ano_y][ano_x-1] == 0 and board[pinned_y][pinned_x-1] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x-1, pinned_y, pinned_x, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                            elif pinned_y < ano_y:
                                if 0 <= ano_x+1 < M and 0 <= pinned_x+1 < M:
                                    if board[ano_y][ano_x+1] == 0 and board[pinned_y][pinned_x+1] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x+1, pinned_y, pinned_x, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                    elif pinned_y == ano_y:
                        # 시계
                        if i == 1:
                            if pinned_x > ano_x:
                                if 0 <= ano_y-1 < N and 0 <= pinned_y-1 < N:
                                    if board[ano_y-1][ano_x] == 0 and board[pinned_y-1][pinned_x] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y-1, pinned_x, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                            elif pinned_x < ano_x:
                                if 0 <= ano_y+1 < N and 0 <= pinned_y+1 < N:
                                    if board[ano_y+1][ano_x] == 0 and board[pinned_y+1][pinned_x] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 =  pinned_x, pinned_y+1, pinned_x, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                        #반시계
                        elif i == 3:
                            if pinned_x > ano_x:
                                if 0 <= ano_y+1 < N and 0 <= pinned_y+1 < N:
                                    if board[ano_y+1][ano_x] == 0 and board[pinned_y+1][pinned_x] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y+1, pinned_x, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
                            elif pinned_x < ano_x:
                                if 0 <= ano_y-1 < N and 0 <= pinned_y-1 < N:
                                    if board[ano_y-1][ano_x] == 0 and board[pinned_y-1][pinned_x] == 0:
                                        rotated_x1, rotated_y1, rotated_x2, rotated_y2 = pinned_x, pinned_y-1, pinned_x, pinned_y
                                        new_cnt += 1
                                        rotated_flag = True
            for j in range(5):
                n_x1, n_x2 = rotated_x1 + dir_x[j], rotated_x2 + dir_x[j]
                n_y1, n_y2 = rotated_y1 + dir_y[j], rotated_y2 + dir_y[j]
                if 0 <= n_x1 < M and 0 <= n_y1 < N and 0 <= n_x2 < M and 0 <= n_y2 < N:
                    if not board[n_y1][n_x1] and not board[n_y2][n_x2]:
                        new_loc = [n_x1, n_y1, n_x2, n_y2]
                        if new_loc not in visited:
                            if j == 4 and rotated_flag:
                                Q.append([n_x1, n_y1, n_x2, n_y2, new_cnt])
                            elif j == 4 and not rotated_flag:
                                continue
                            else:
                                Q.append([n_x1, n_y1, n_x2, n_y2, new_cnt+1])
                                
                            visited.append(new_loc)

    
    return res

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
res = solution(board)
print(res)

