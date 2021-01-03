n = int(input())

dp = [0 for i in range(100001)]

dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = 10000000
    for j in range(1, i+1):
        if j ** 2 > i:
            break;
        else:
            dp[i] = min(dp[i], dp[i-j**2] + 1)

print(dp[n])