N = int(input())
arr = []
count0, count1, countm1 = 0, 0, 0
for i in range(N):
    arr.append(list(map(int, input().split())))

def solve(size, x, y):
    global count0, count1, countm1
    check = False
    f_num = arr[y][x]
    for i in range(y, y+size):
        for j in  range(x, x+size):
            if arr[i][j] != f_num:
                check = True
        if check:
            break
    if check:
        new_size = size // 3
        solve(new_size, x, y)
        solve(new_size, x+new_size, y)
        solve(new_size, x+new_size*2, y)
        solve(new_size, x, y+new_size)
        solve(new_size, x+new_size, y+new_size)
        solve(new_size, x+new_size*2, y+new_size)
        solve(new_size, x, y+new_size*2)
        solve(new_size, x+new_size, y+new_size*2)
        solve(new_size, x+new_size*2, y+new_size*2)
    else:
        if f_num == 0:
            count0 += 1
        elif f_num == 1:
            count1 += 1
        elif f_num == -1:
            countm1 += 1
solve(N, 0, 0)
print(countm1)
print(count0)
print(count1)