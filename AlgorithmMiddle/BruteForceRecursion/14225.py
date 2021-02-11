N = int(input())
s = list(map(int, input().split()))
check = [False for i in range(20*100000)]
MIN = min(s)
MAX = max(s)

def solve(SUM, cnt):    

    if cnt == N:
        check[SUM] = True
        return

    solve(SUM + s[cnt], cnt+1)
    solve(SUM, cnt+1)

solve(0, 0)

tmp = 0
flag = False

for i in range(20*100000):
    if check[i]:
        flag = True
    else:
        if flag:
            print(i)
            break
