n = int(input())
arr = list(map(int, input().split()))
dp = [[-1001 for i in range(100001)] for j in range(2)]

arr.insert(0,0)

ans = arr[1]

for i in range(1,n+1):
    dp[0][i] = dp[1][i] = arr[i]

for i in range(2,n+1):
    dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])
    ans = max(ans, dp[0][i], dp[1][i])

print(ans)

