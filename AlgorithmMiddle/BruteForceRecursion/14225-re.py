N = int(input())
s = list(map(int, input().split()))

check = [False for i in range(20*100000+1)]

def solve(sum, cnt):
    if cnt == N:
        check[sum] = True
        return
    
    solve(sum + s[cnt], cnt + 1)
    solve(sum, cnt + 1)

solve(0, 0)

flag = False    

for i in range(20*100000+1):
    if check[i]:
        flag = True
    else:
        if flag:
            print(i)
            break