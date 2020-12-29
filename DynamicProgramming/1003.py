T = int(input())

mem = [0 for i in range(41)]
cnt0 = [0 for i in range(41)]
cnt1 = [0 for i in range(41)]

def fibonacci(n):
    if n == 0:
        cnt0[n] = 1
        return 0
    elif n == 1:
        cnt1[n] = 1
        return 1
    elif mem[n] != 0:
        return mem[n]
    mem[n] = fibonacci(n-1) + fibonacci(n-2)
    cnt0[n] = cnt0[n-1] + cnt0[n-2]
    cnt1[n] = cnt1[n-1] + cnt1[n-2]

    return mem[n]

for i in range(T):
    num = int(input())
    fibonacci(num)
    print(cnt0[num], cnt1[num])
    mem = [0 for i in range(41)]