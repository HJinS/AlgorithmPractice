N = int(input())
coins = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    inp = list(input())
    for j in range(N):
        if inp[j] == 'H':
            coins[i][j] = 1


def convert(loc):
    for i in range(N):
        coins[loc][i] = 1 - coins[loc][i]

def flip(cnt):
    if cnt == N:
        total = 0
        for i in range(N):
            col_min = 0
            for j in range(N):
                if coins[j][i] == 0:
                    col_min += 1
            total += min(col_min, N-col_min)
        return total
    
    res1 = flip(cnt+1)
    convert(cnt)
    res2 = flip(cnt+1)
    return min(res1, res2)

res = flip(0)
print(res)