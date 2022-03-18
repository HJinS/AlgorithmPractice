class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def is_Interleave(s1, i, s2, j, res, s3):
            if res == s3 and i == len(s1) and j == len(s2):
                return True
            ans = False
            
            if i < len(s1):
                # s1다음을 확인
                ans |= is_Interleave(s1, i+1, s2, j, res+s1[i], s3)
            if j < len(s2):
                # s2다음을 확인
                ans |= is_Interleave(s1, i, s2, j+1, res+s2[j], s3)
            return ans
        
        if len(s1) + len(s2) != len(s3):
            return False
        return is_Interleave(s1, 0, s2, 0, "", s3)
            
    
        def ans_with_2D_dp():
            if len(s3) != len(s1) + len(s2):
                return False
            # dp 초기화 s1에서 i까지 s2에서 j까지 확인함
            dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
            
            for i in range(len(s1)+1):
                for j in range(len(s2)+1):
                    # 0, 0일경우는 True로 지정
                    if i == 0 and j == 0:
                        dp[i][j] = True
                    
                    elif i == 0:
                        dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                    else:
                        dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
                        
            return dp[len(s1)-1][len(s2)-1]
        
        def ans_with_1D_dp():
            if len(s3) != len(s1) + len(s2):
                return False

            dp = [False for i in range(len(s2)+1)]
            
            for i in range(len(s1)+1):
                for j in range(len(s2)+1):
                    # 0, 0일경우는 True로 지정
                    if i == 0 and j == 0:
                        dp[j] = True
                    
                    elif i == 0:
                        dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                    elif j == 0:
                        dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
                    else:
                        dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
                        
            return dp[len(s2)]