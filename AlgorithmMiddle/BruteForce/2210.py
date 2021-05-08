nums = []
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
for i in range(5):
    nums.append(list(map(int, input().split())))

res = []

def solve(x, y, cnt, num):
    if cnt == 6:
        if num in res:
            pass
        else:
            res.append(num)
        return
    for i in range(4):
        n_x = x + dir_x[i]
        n_y = y + dir_y[i]
        if 0 <= n_x < 5 and 0 <= n_y < 5:
            solve(x+dir_x[i], y+dir_y[i], cnt+1, num*10+nums[y][x])

for i in range(5):
    for j in range(5):
        solve(i, j, 0, 0)

print(len(res))