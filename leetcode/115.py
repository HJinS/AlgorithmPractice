class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)

        dp1 = [[0 for i in range(m+1)]for j in range(n+1)]
        
        for i in range(n+1):
            dp1[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                # s#i == t#j 일경우 dp[i-1][j-1]와 dp[i-1][j]를 더함
                # j까지 확인한 것을 더해야하는데 j-1까지 확인한 것에 j를 추가하거나
                # j까지 확인한 것에(s는 i-1)을 그대로 가져오거나
                if s[i-1] == t[j-1]:
                    dp1[i][j] = dp1[i-1][j-1] + dp1[i-1][j]
                else:
                    dp1[i][j] = dp1[i-1][j]
            
        return dp1[n][m]