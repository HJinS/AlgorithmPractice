import sys

N = int(input())
coins = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    inp = input()
    for j in range(N):
        if inp[j] == 'H':
            coins[i][j] = 1

def convert_row(loc):
        for i in range(N):
            coins[loc][i] = 1 - coins[loc][i]

def flip(row):
    if row == N:
        total = 0
        for i in range(N):
            col_cnt = 0
            for j in range(N):
                if coins[j][i] == 0:
                    col_cnt += 1
            total += min(col_cnt, N-col_cnt)
        return total
    unfliped_cnt = flip(row+1)
    convert_row(row)
    fliped_cnt = flip(row+1)
    return min(unfliped_cnt, fliped_cnt)
    

res = flip(0)
print(res)