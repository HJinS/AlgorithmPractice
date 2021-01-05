n = int(input())
dp = [[0 for i in range(100000)] for j in range(2)]

dp[0][0] = 1
dp[1][0] = 2
dp[0][1] = 3
dp[1][1] = 4

for i in range(2,n):
    dp[0][i] = (dp[0][i-1] + dp[1][i-1])%9901
    dp[1][i] = (dp[1][i-1] + 2*(dp[1][i-2] + dp[0][i-2]))%9901
print((dp[0][n-1] + dp[1][n-1])%9901)