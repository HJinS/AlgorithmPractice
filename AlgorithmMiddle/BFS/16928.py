from collections import deque
N, M = map(int, input().split())
ladder_snake = {}
board = [i for i in range(101)]
visited = [False for i in range(101)]
res = 987654321

for i in range(N+M):
    s, d = map(int, input().split())
    ladder_snake[s] = d

def BFS():
    global res
    Q = deque()
    Q.append([1, 0])
    visited[1] = True
    while Q:
        e = Q.popleft()
        loc = e[0]
        cnt = e[1]
        if loc == 100:
            res = min(res, cnt)
        for i in range(1, 7):
            new_loc = loc + i
            if new_loc <= 100:
                if new_loc in ladder_snake:
                    new_loc = ladder_snake[new_loc]
                if not visited[new_loc]:
                    visited[new_loc] = True
                    Q.append([new_loc, cnt + 1])

BFS()
print(res)


