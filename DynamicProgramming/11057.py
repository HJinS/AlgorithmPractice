n = int(input())

dp = [[0 for i in range(1001)] for j in range(10)]

dp[0][1] = 1
dp[1][1] = 1
dp[2][1] = 1
dp[3][1] = 1
dp[4][1] = 1
dp[5][1] = 1
dp[6][1] = 1
dp[7][1] = 1
dp[8][1] = 1
dp[9][1] = 1

for i in range(2,n+1):
    for j in range(10):
        for k in range(j+1):
            dp[j][i] += dp[k][i-1]
            dp[j][i] %= 10007

res = 0
for i in range(10):
    res += dp[i][n]
    res %= 10007

print(res)