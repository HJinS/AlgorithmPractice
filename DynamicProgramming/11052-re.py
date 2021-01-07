n = int(input())
card = list(map(int, input().split()))
dp = [0 for i in range(1001)]

card.insert(0,0)

dp[0] = 0
dp[1] = card[1]

for i in range(2,n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + card[j])
print(dp[n])