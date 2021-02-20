from collections import deque
import copy, sys
T = int(input())
op = ['D', 'S', 'L', 'R']
visited = [False for i in range(10000)]
res = ''

def operate(num, op_char):
    input_num = num
    if op_char == 'D':
        res_num = input_num * 2
        if res_num >= 10000:
            res_num %= 10000
    elif op_char == 'S':
        res_num = input_num - 1
        if res_num < 0:
            res_num = 9999
    elif op_char == 'L':
        len_num = len(str(input_num))
        if len_num != 4:
            res_num = input_num * 10
        else:
            first, last = divmod(input_num, (10 ** (len_num-1)))
            res_num = first + last * 10
    elif op_char == 'R':
        len_num = len(str(input_num))
        if len_num == 1:
            res_num = input_num * 1000
        else:
            first, last = divmod(input_num, 10)
            res_num = first + last * 1000
    return res_num

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
            new_num = operate(num, op[i])
            if new_num >= 0 and new_num < 10000 and not visited[new_num]:
                visited[new_num] = True
                Q.append([new_num, cmd+op[i]])
                
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visited = [False for i in range(10000)]
    res = BFS()
    print(res)