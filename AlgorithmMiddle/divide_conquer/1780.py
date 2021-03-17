import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())
arr = []
count0, count1, countm1 = 0, 0, 0
for i in range(N):
    arr.append(list(map(int, input().split())))

def solve(x, y, n):
    global count0, count1, countm1
    flag = arr[y][x]
    check = False
    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[i][j] != flag:
                check = True
        if check:
            break
    if check:
        solve(x, y, n//3)
        solve(x+n//3, y, n//3)
        solve(x+(n//3)*2, y, n//3)
        solve(x, y+n//3, n//3)
        solve(x+n//3, y+n//3, n//3)
        solve(x+(n//3)*2, y+n//3, n//3)
        solve(x, y+(n//3)*2, n//3)
        solve(x+n//3, y+(n//3)*2, n//3)
        solve(x+(n//3)*2, y+(n//3)*2, n//3)
    else:
        if flag == -1:
            countm1 += 1
        elif flag == 0:
            count0 += 1
        elif flag == 1:
            count1 += 1

solve(0, 0, N)
print(countm1)
print(count0)
print(count1)