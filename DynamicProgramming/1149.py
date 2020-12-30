n = int(input())

RGB = [[0 for col in range(1001)]for row in range(3)]
dp = [[0 for col in range(1001)]for row in range(3)]

#  0-R 1-G 2-B

for i in range(1,n+1):
    RGB[0][i], RGB[1][i], RGB[2][i] = map(int, input().split())

dp[0][1] = RGB[0][1]
dp[1][1] = RGB[1][1]
dp[2][1] = RGB[2][1]

for i in range(1,n+1):
    dp[0][i] = min(dp[1][i-1] + RGB[1][i],dp[2][i-1] + RGB[2][i])
    dp[1][i] = min(dp[0][i-1] + RGB[0][i],dp[2][i-1] + RGB[2][i])
    dp[2][i] = min(dp[0][i-1] + RGB[0][i],dp[1][i-1] + RGB[1][i])

print(min(dp[0][n], dp[1][n], dp[2][n]))
