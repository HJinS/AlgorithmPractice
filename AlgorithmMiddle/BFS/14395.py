from collections import deque
s, t = map(int, input().split())
visited = set()
MAX = 10e9
def BFS():
    global s, t
    Q = deque()
    Q.append([s, ''])
    if s == t:
        return 0
    while Q:
        num, cal = Q.popleft()
        if num == t:
            return cal
        n_num = int(num * num)
        if 1 <= n_num <= MAX and n_num not in visited:
            Q.append([n_num, cal+'*'])
            visited.add(n_num)
        n_num = num + num
        if 1 <= n_num <= MAX and n_num not in visited:
            Q.append([n_num, cal+'+'])
            visited.add(n_num)
        n_num = int(num // num)
        if 1 <= n_num <= MAX and n_num not in visited:
            Q.append([n_num, cal+'/'])
            visited.add(n_num)
    return -1

res = BFS()
print(res)