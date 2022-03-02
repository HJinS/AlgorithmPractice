
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid[0])
        N = len(obstacleGrid)
        dp = [[0 for i in range(M)] for j in range(N)]
        
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        
        for i in range(N):
            for j in range(M):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[N-1][M-1]