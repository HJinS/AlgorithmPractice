n = int(input())
dp = [[0 for col in range(91)]for row in range(2)]
dp[0][0] = 0
dp[0][1] = 0
dp[1][1] = 1
dp[0][2] = 1
dp[1][2] = 0

for i in range(3,n+1):
    dp[0][i] = dp[0][i-1] + dp[1][i-1]
    dp[1][i] = dp[0][i-1]

print(dp[0][n] + dp[1][n])