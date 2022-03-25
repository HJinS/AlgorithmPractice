from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 우 하 좌 우
        dir_x = [1, 0, -1, 0]
        dir_y = [0, 1, 0, -1]
        
        res = [[-1 for i in range(n)] for j in range(n)]
        x, y = 0, 0
        res[0][0] = 1
        direction = 0
        cnt = 1
        while cnt <= n * n:
            
            res[y][x] = cnt
            cnt += 1
            n_x = x+dir_x[direction]
            n_y = y+dir_y[direction]
            if cnt > n * n:
                break
            
            if 0 <= n_x < n and 0 <= n_y < n and res[n_y][n_x] == -1:
                x, y = n_x, n_y
            else:
                direction += 1
                if direction == 4:
                    direction = 0
                n_x = x+dir_x[direction]
                n_y = y+dir_y[direction]
                x, y = n_x, n_y
                    
                
            
        return res