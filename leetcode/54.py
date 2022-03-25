from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 우 하 좌 우
        dir_x = [1, 0, -1, 0]
        dir_y = [0, 1, 0, -1]
        
        M, N = len(matrix), len(matrix[0])
        visited = [[False for i in range(N)] for j in range(M)]
        x, y = 0, 0
        res = []
        direction = 0
        visited[0][0] = True
        cnt = 0
        while cnt < M * N:
            res.append(matrix[y][x])
            cnt += 1
            n_x = x+dir_x[direction]
            n_y = y+dir_y[direction]
            if cnt >= N * M:
                break
            
            if 0 <= n_x < N and 0 <= n_y < M and not visited[n_y][n_x]:
                visited[n_y][n_x] = True
                x, y = n_x, n_y
            else:
                direction += 1
                if direction == 4:
                    direction = 0
                n_x = x+dir_x[direction]
                n_y = y+dir_y[direction]
                visited[n_y][n_x] = True
                x, y = n_x, n_y
                    
                
            
        return res