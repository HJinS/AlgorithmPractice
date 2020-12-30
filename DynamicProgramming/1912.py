n = int(input())

arr = list(map(int, input().split()))
dp = [[0 for col in range(n)]for row in range(2)]

dp[0][0] = arr[0]
dp[1][0] = arr[0]
for i in range(1, n):
    dp[0][i] = max(dp[1][i-1], dp[0][i-1], arr[i])
    dp[1][i] = max(dp[1][i-1] + arr[i], arr[i])

print(max(dp[0][n-1], dp[1][n-1]))