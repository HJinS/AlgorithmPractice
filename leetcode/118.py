class Solution:
    def generate(self, numRows: int):
        res = []
        
        for i in range(numRows):
            res.append([0 for k in range(i+1)])
        res[0][0] = 1
        
        for i in range(numRows):
            res[i][0] = 1
            res[i][i] = 1
            
        if numRows <= 1:
            return res
            
        for i in range(2, numRows):
            for j in range(i+1):
                if i != 0 and j != 0 and j != i:
                    res[i][j] = res[i-1][j-1] + res[i-1][j]
                    
        return res