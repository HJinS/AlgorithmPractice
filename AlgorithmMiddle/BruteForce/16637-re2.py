import sys
#틀림
sys.setrecursionlimit(int(10e6))
N = int(input())
num, op = [], []
formula = list(input())
res = 0
for e in formula:
    if e != '+' and e != '-' and e != '*':
        num.append(e)
    else:
        op.append(e)

def solve(idx, total):
    global res
    if idx == len(op):
        res = max(res, int(total))
        return
    
    first = str(eval(total + op[idx] + num[idx+1]))
    solve(idx+1, first)

    if idx + 1 < len(op):
        second = str(eval(num[idx+1] + op[idx+1] + num[idx+2]))
        second = str(eval(total + op[idx] + second))
        solve(idx+2, second)

solve(0, num[0])
print(res)