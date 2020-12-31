#복습 한번 해 볼 것

n = int(input())

P = list(map(int, input().split()))
dp = [0 for i in range(1001)]

P.insert(0,0)

dp[1] = P[1]

for i in range(1,n+1):
    dp[i] = P[i]

for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[n])
