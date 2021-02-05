from collections import deque
S = int(input())

visited = [[False for i in range(1001)] for j in range(1001)]
op = [1, 2, 3]

def BFS():
    Q = deque()
    Q.append([1, 0, 0])
    visited[1][0] = True
    while Q:
        e = Q.popleft()
        imo = e[0]
        cnt = e[1]
        clip_board = e[2]
        if imo == S:
            return cnt

        for i in range(3):
            if op[i] == 1:
                new_imo = imo
                new_clip = imo
            elif clip_board != 0 and op[i] == 2:
                new_imo = imo + clip_board
                new_clip = clip_board
            elif op[i] == 3:
                new_imo = imo - 1
                new_clip = clip_board
            
            if new_imo >= 1 and new_imo <= 1000 and not visited[new_imo][new_clip]:
                Q.append([new_imo, cnt + 1, new_clip])
                visited[new_imo][new_clip] = True
res = BFS()
print(res)