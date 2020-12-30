n = int(input())

dp = [0 for i in range(101)]

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3

## 초기화 어디까지 할 지
## 쉬운문제니 잘 볼 것

for i in range(7, 101):
    dp[i] = dp[i - 5] + dp[i-1]

for i in range(n):
    num = int(input())
    print(dp[num])

    