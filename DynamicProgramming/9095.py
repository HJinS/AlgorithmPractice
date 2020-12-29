T = int(input())
dp = [0,1,2,4]
for k in range(4,11):
        dp.insert(k, dp[k-1] + dp[k-2] + dp[k-3])
for i in range(T):
    n = int(input())
    print(dp[n])