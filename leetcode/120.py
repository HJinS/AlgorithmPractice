class Solution:
    def minimumTotal(self, triangle) -> int:
        N = len(triangle)
        dp = [[0 for i in range(j+1)] for j in range(N)]
        dp[0][0] = triangle[0][0]

        for i in range(1, N):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                
        return min(dp[N-1])