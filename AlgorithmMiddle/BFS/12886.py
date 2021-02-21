from collections import deque
n1, n2, n3 = map(int, input().split())
visited = [[False for i in range(1501)] for j in range(1501)]
total = n1 + n2 + n3

def BFS():
    global n1, n2, n3, total
    Q = deque()
    Q.append([n1, n2])
    visited[n1][n2] = True

    while Q:
        a, b = Q.popleft()
        c = total - a - b
        if a == b and b == c:
            return 1
        for n_a, n_b in [[a, b], [b, c], [a, c]]:
            if n_a < n_b:
                n_b -= n_a
                n_a += n_a
            elif n_a > n_b:
                n_a -= n_b
                n_b += n_b
            else:
                continue
            n_c = total - n_a - n_b
            min_n = min(n_a, n_b, n_c)
            max_n = max(n_a, n_b, n_c)
            if not visited[min_n][max_n]:
                visited[min_n][max_n] = True
                Q.append([min_n, max_n])
    return 0

res = BFS()
print(res)