import sys
n = int(input())
arr = list(map(str, input().split()))

visited = [False for i in range(10)]
res = [0 for i in range(n+1)]

maxNum = -sys.maxsize - 1
minNum = sys.maxsize

ans1 = [0 for i in range(n+1)]
ans2 = [0 for i in range(n+1)]

def solve(cnt):
    global maxNum
    global minNum
    global ans1
    global ans2
    if cnt == n+1:
        num = 0
        for i in range(n+1):
            num += res[i] * (10**(len(res)-i-1))
        if maxNum < num:
            ans1 = res[:]
            maxNum = num
        if minNum > num:
            ans2 = res[:]
            minNum = num
        return

    for j in range(9,-1,-1):
        if cnt == 0:
            if visited[j] == False:
                visited[j] = True
                res[cnt] = j
                solve(cnt+1)
                visited[j] = False
        elif cnt != 0 and arr[cnt-1] == '<':
            if j > res[cnt-1] and visited[j] == False:
                visited[j] = True
                res[cnt] = j
                solve(cnt+1)
                visited[j] = False
            else:
                continue
        elif cnt != 0 and arr[cnt-1] == '>':
            if j < res[cnt-1] and visited[j] == False:
                visited[j] = True
                res[cnt] = j
                solve(cnt+1)
                visited[j] = False
            else:
                continue 

solve(0)
for i in range(n+1):
    print(ans1[i],end='')
print()
for i in range(n+1):
    print(ans2[i],end='')
print()