n = int(input())
dp = [0 for i in range(n+1)]
stair = []
for i in range(n):
    stair.append(int(input()))
stair.insert(0,0)

dp[0] = 0
dp[1] = stair[1]

for i in range(2,n+1):
    dp[i] = max(dp[i-3] + stair[i-1], dp[i-2])
    dp[i] += stair[i]

print(dp[n])