from collections import deque
def solution(maps):
    
    Q = deque()
    Q.append([0, 0, 1])
    N, M = len(maps), len(maps[0])
    dir_x, dir_y = [1, 0, -1, 0], [0, 1, 0, -1]
    visited = [[False for j in range(M)] for i in range(N)]
    ans = N*M
    flag = False
    while Q:
        x, y, cnt = Q.popleft()
        if x == M-1 and y == N-1:
            ans = min(ans, cnt)
            flag =  True
        for i in range(4):
            n_x, n_y = x+dir_x[i], y+dir_y[i]
            if 0 <= n_x < M and 0 <= n_y < N:
                if maps[n_y][n_x] == 1:
                    if not visited[n_y][n_x]:
                        visited[n_y][n_x] = True
                        Q.append([n_x, n_y, cnt+1])
    
    
    if flag:
        return ans
    else:
        return -1