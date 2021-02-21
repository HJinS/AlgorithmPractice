from collections import deque
T = int(input())
op_type = ['D', 'S', 'L', 'R']

def operate(num, type):
    if type == 'D':
        res = num * 2
        if res >= 10000:
            res = res % 10000
    elif type == 'S':
        res = num - 1
        if res < 0:
            res = 9999
    elif type == 'L':
        digit = len(str(num))
        if digit != 4:
            res = num * 10
        else:
            l, r = divmod(num, 10 ** 3)
            res = l + r * 10
    elif type == 'R':
        digit = len(str(num))
        if digit == 1:
            res = num * 1000
        else:
            l, r = divmod(num, 10)
            res = l + r * 1000
    return res

def BFS():
    global A, B
    Q = deque()
    Q.append([A, ''])
    visited[A] = True

    while Q:
        num, cmd = Q.popleft()
        if num == B:
            return cmd
        for i in range(4):
            new_num = operate(num, op_type[i])
            if not visited[new_num]:
                visited[new_num] = True
                Q.append([new_num, cmd+op_type[i]])

for i in range(T):
    A, B = map(int, input().split())
    visited = [False for i in range(10000)]
    res = BFS()
    print(res)