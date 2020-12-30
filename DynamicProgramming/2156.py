n = int(input())

wine = [0 for i in range(10001)]
dp = [[0 for col in range(10001)]for row in range(2)]

for i in range(1,n+1):
    wine[i] = int(input())

# 0 - i번째 와인 안마셨다 1 - 마셨다

dp[0][1] = 0
dp[1][1] = wine[1]
dp[0][2] = wine[1]
dp[1][2] = wine[1] + wine[2]

for i in range(3,n+1):
    dp[0][i] = max(dp[1][i-1], dp[0][i-1])
    dp[1][i] = max(dp[1][i-2] + wine[i], dp[0][i-2] + wine[i-1] + wine[i])

print(max(dp[0][n], dp[1][n]))