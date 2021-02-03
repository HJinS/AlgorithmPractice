from collections import deque
N, K = map(int, input().split())
direction = [1, -1, 2]
visited = [False for i in range(100001)]

def BFS(start, des):
    Q = deque()
    Q.append(start)
    cnt = 0
    visited[start] = True
    while Q:
        for k in range(len(Q)):
            e = Q.popleft()

            if e == des:
                return cnt
            for i in range(3):
                if direction[i] == 2:
                    next_loc = e * direction[i]
                else:
                    next_loc = e + direction[i]

                if next_loc <= 100000 and next_loc >= 0 and not visited[next_loc]:
                    Q.append(next_loc)
                    visited[next_loc] = True
        cnt += 1

res = BFS(N, K)
print(res)