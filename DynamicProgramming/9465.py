T = int(input())

for i in range(T):
    n = int(input())
    P = []
    dp = [[0 for col in range(n)]for row in range(2)]
    P.append(list(map(int, input().split())))
    P.append(list(map(int, input().split())))

    for j in range(n):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + P[0][j]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + P[1][j]
    print(max(dp[0][n-1], dp[1][n-1]))



    