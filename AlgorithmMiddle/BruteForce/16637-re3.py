N = int(input())

formula = [int(x) if x.isdigit() else x for x in input().strip()]

def cal_Q(Q):
    res = Q[0]
    for i in range(1, len(Q), 2):
        post = Q[i+1]
        res = cal(res, Q[i], post)
    return res

def cal(l, op, r):
    if op == '+':
        return l + r
    elif op == '-':
        return l - r
    elif op == '*':
        return l * r

def bracket(idx, Q):
    if idx == N-1:
        no_br = Q + [formula[idx]]
        return cal_Q(no_br)
    if idx == N-3:
        no_br = Q + [formula[idx], formula[idx+1]]
        tmp = cal(formula[idx], formula[idx+1], formula[idx+2])
        br = Q + [tmp]
        return max(bracket(idx+2, no_br), cal_Q(br))

    no_br = Q + [formula[idx], formula[idx+1]]
    tmp = cal(formula[idx], formula[idx+1], formula[idx+2])
    br = Q + [tmp, formula[idx+3]]
    return max(bracket(idx+2, no_br), bracket(idx+4, br))

res = bracket(0, [])
print(res)