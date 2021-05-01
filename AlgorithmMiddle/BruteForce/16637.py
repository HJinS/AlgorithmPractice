import sys
sys.setrecursionlimit(10**6)

def cal_queue(Q):
    res = Q[0]
    for i in range(0, len(Q)-2, 2):
        post = Q[i+2]
        res = cal_nums(res, post, Q[i+1])
    return res

def cal_nums(pre, post, op):
    if op == '+':
        return pre + post
    elif op == '-':
        return pre - post
    else:
        return pre * post

def insert_bracket(i,  q):
    if i == n-1:
        no_br = q + [f[i]]
        return cal_queue(no_br)
    if i == n-3:
        no_br = q + [f[i], f[i+1]]
        tmp = cal_nums(f[i], f[i+2], f[i+1])
        br = q + [tmp]
        return max(insert_bracket(i+2, no_br), cal_queue(br))
    
    no_br = q + [f[i], f[i+1]]
    tmp = cal_nums(f[i], f[i+2], f[i+1])
    br = q + [tmp, f[i+3]]

    return max(insert_bracket(i+2, no_br), insert_bracket(i+4, br))

n = int(input())
f = [int(x) if x != '+' and x != '-' and x != '*' else x for x in input().strip()]
print(insert_bracket(0, []))