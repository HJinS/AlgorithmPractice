from collections import deque
S = int(input())

res = 987654321
cal = [i+1 for i in range(3)]
visited = [[False for i in range(S+1)] for j in range(S+1)]

def BFS():
    global S
    global res
    Q = deque()
    Q.append([1, 0, 0])
    visited[1][0] = True
    while Q:
        e = Q.popleft()
        imoti = e[0]
        time = e[1]
        clip_board = e[2]
        if imoti == S:
            return
        for i in range(3):
            if cal[i] == 1:
                new_clip_board = imoti
                next_e = imoti
            elif clip_board != 0 and cal[i] == 2:
                next_e = imoti + clip_board
                new_clip_board = clip_board
            elif imoti != 0 and cal[i] == 3:
                next_e = imoti -1
                new_clip_board = clip_board

            if next_e >= 0 and next_e <= S and not visited[next_e][new_clip_board]:
                if next_e == S:
                    res = min(res, time+1)
                Q.append([next_e, time+1, new_clip_board])
                visited[next_e][new_clip_board] = True

BFS()

print(res)