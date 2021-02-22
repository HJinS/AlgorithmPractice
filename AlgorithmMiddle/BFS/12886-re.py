from collections import deque

n1, n2, n3 = map(int, input().split())
visited = [[False for i in range(1501)] for j in range(1501)]
total = n1 + n2 + n3

def BFS():
    global n1, n2, n3, total
    Q = deque()
    Q.append([n1, n2])

    while Q:
        A, B = Q.popleft()
        C = total - A - B
        if A == B and B == C:
            return 1
        for n_A, n_B in [[A, B], [B, C], [A, C]]:
            if n_A < n_B:
                n_B -= n_A
                n_A += n_A
            elif n_A > n_B:
                n_A -= n_B
                n_B += n_B
            else:
                continue
            n_C = total - n_A - n_B
            n_min = min(n_A, n_B, n_C)
            n_max = max(n_A, n_B, n_C)
            if not visited[n_min][n_max]:
                visited[n_min][n_max] = True
                Q.append([n_min, n_max])
    return 0

res = BFS()
print(res)