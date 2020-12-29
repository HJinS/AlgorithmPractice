n = int(input())
dp = [-1,0,1,1]

def dpCalc():
    for i in range(4,n+1):
        if i%2 == 0 and i%3 == 0:
            dp.insert(i, min(dp[i//3],dp[i//2],dp[i-1]) + 1)
        elif i%2 == 0:
            dp.insert(i, min(dp[i//2],dp[i-1]) + 1)
        elif i%3 == 0:
            dp.insert(i, min(dp[i//3],dp[i-1]) + 1)
        else:
            dp.insert(i, dp[i-1] + 1)

dpCalc()
print(dp[n])