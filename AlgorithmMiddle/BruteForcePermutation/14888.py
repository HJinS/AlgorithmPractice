import sys

sys.setrecursionlimit(100000)
N = int(input())
operand = list(map(int, input().split()))
operator = list(map(int, input().split()))
res = 0
rMax = -10000000000
rMin = 10000000000

def solve(num):
    global res, rMax, rMin
    if num == 0:
       res = operand[num] 
    if num == N-1:
        rMax = max(rMax, res)
        rMin = min(rMin, res)
        return
    
    for i in range(4):
        if operator[i] == 0:
            continue
        tmp = res
        if i == 0:
            res = int(res + operand[num+1])
        elif i == 1:
            res = int(res - operand[num+1])
        elif i == 2:
            res = int(res * operand[num+1])
        elif i == 3:
            if res < 0:
                res = int(abs(res) // operand[num+1])
                res *= -1
            else:
                res = int(res // operand[num+1])
        operator[i] -= 1
        solve(num + 1)
        operator[i] += 1
        res = tmp
solve(0)
print(rMax)
print(rMin)
