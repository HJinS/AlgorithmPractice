from collections import deque
N, K = map(int, input().split())
visited = [0 for i in range(100001)]
next_dir = [1, -1, 2]
res = 987654321

def BFS(start, des):
    global res
    Q = deque()
    Q.append([start,0])
    visited[start] = 1
    while Q:
        
        for i in range(len(Q)):
            e = Q.popleft()
            loc = e[0]
            time = e[1]

            if loc == des:
                res = min(res, time)

            for i in range(3):
                if next_dir[i] == 2:
                    next_e = loc * 2
                    next_time = time
                else:
                    next_e = loc + next_dir[i]
                    next_time = time + 1

                if next_e >= 0 and next_e <= 100000 and visited[next_e] <= 3:
                    visited[next_e] += 1
                    Q.append([next_e, next_time])
BFS(N, K)
print(res)