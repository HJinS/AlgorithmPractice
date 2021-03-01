N = int(input())
bulb = list(map(int, input()))
goal = list(map(int, input()))

def solve(bulb):
    cnt = 1
    bulb[0] = 1 - bulb[0]
    bulb[1] = 1 - bulb[1]
    for i in range(1, N):
        if bulb[i-1] != goal[i-1]:
            cnt += 1
            bulb[i-1] = 1 - bulb[i-1]
            bulb[i] = 1 - bulb[i]
            if i != N-1:
                bulb[i+1] = 1 - bulb[i+1]
    if bulb == goal:
        return cnt
    else:
        return -1

def solve_nonClick(bulb):
    cnt = 0
    for i in range(1, N):
        if bulb[i-1] != goal[i-1]:
            cnt += 1
            bulb[i-1] = 1 - bulb[i-1]
            bulb[i] = 1 - bulb[i]
            if i != N-1:
                bulb[i+1] = 1 - bulb[i+1]
    if bulb == goal:
        return cnt
    else:
        return -1

res1 = solve(bulb[:])
res2 = solve_nonClick(bulb[:])
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print("-1")