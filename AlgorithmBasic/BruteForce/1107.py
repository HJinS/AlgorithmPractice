
n = int(input())
m = int(input())
btn = [True for i in range(10)]
if m != 0:
    worngBtn = list(map(int, input().split()))
    for w in worngBtn:
        btn[w] = False

def check(n):
    if n == 0:
        if btn[n]:
            return 1
        else:
            return 0
    len = 0
    while n>0:
        if btn[int(n%10)] == False:
            return 0
        n = n // 10
        len += 1
    return len

result = abs(n-100)

for i in range(1000000 + 1):
    c = i
    len = check(c)
    if len > 0:
        press = abs(c-n)
        result = min(result, press + len)

print(result)