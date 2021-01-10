n = int(input())
m = int(input())
Btn = [True for i in range(10)]

if m != 0:
    wBtn = list(map(int, input().split()))    
    for btn in wBtn:
        Btn[btn] = False

def check(num):
    c = num
    if c // 10 == 0:
        if Btn[c] == False:
            return 0
        else:
            return 1
    len = 0
    while c > 0:
        remain = c % 10
        c = c // 10
        if Btn[remain] == False:
            return 0
        else:
            len += 1
        
    return len

res = abs(n - 100)

for i in range(1000001):
    num = i
    len = check(num)
    if len != 0:
        press = abs(num-n)
        res = min(res, len + press)
print(res)