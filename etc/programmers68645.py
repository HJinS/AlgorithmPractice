
def solution(n):
    l = [[-1 for i in range(j+1)] for j in range(n)]

    total_cnt = 0
    for i in range(1, n+1):
        total_cnt += i
    direction = [0, 1]
    cnt = 1
    x, y = 0, 0
    y_len = n
    while cnt <= total_cnt:
        x_dir, y_dir = direction
        if x_dir == 0:
            while 0 <= y < y_len:
                if l[y][x] == -1:
                    l[y][x] = cnt
                    cnt += 1
                y += y_dir
                if y_dir < 0:
                    x -= 1
                if 0 <= y < n and l[y][x] != -1:
                    break
            if y_dir > 0:
                y -= 1
            else:
                y += 1
                x += 1
        elif y_dir == 0:
            flag = False
            while 0 <= x < len(l[y]):
                if l[y][x] == -1:
                    l[y][x] = cnt
                    cnt += 1
                elif flag:
                    break
                if not flag:
                    flag = True
                x += x_dir

            x -= 1
        if direction == [0, 1]:
            direction = [1, 0]
        elif direction == [1, 0]:
            direction = [0, -1]
        elif direction == [0, -1]:
            direction = [0, 1]
    return sum(l, [])