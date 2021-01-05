n = int(input())

dp = [[0 for i in range(100)] for j in range(100)]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        tmp = arr[i][j]
        if i == n-1 and j == n-1:
            break
        if i + tmp < n:
            dp[i+tmp][j] += dp[i][j]
            
        if j + tmp < n:
            dp[i][j+tmp] += dp[i][j]
            
print(dp[n-1][n-1])