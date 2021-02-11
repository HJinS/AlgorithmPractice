N = int(input())
operand = list(map(int, input().split()))
operator = list(map(int, input().split()))
res = 0
rMax = -1000000000
rMin = 1000000000

def solve(cnt):
    global res, rMax, rMin
    if cnt == 0:
        res = operand[0]

    if cnt == N-1:
        rMax = max(rMax, res)
        rMin = min(rMin, res)
        return

    for i in range(4):
        if operator[i] == 0:
            continue
        tmp = res
        if i == 0:
            res = res + operand[cnt + 1]
        elif i == 1:
            res = res - operand[cnt + 1]
        elif i == 2:
            res = int(res * operand[cnt + 1])
        elif i == 3:
            if res < 0:
                res = int(abs(res) // operand[cnt + 1])
                res *= -1
            else:
                res = int(res // operand[cnt + 1])
        
        operator[i] -= 1
        solve(cnt + 1)
        operator[i] += 1
        res = tmp
solve(0)
print(rMax)
print(rMin)