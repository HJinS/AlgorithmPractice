#복습 필요
s1 = input()
s2 = input()

dp = [[0 for i in range(1001)] for j in range(1001)]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(s1)-1][len(s2)-1])
