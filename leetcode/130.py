from collections import deque
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
                       
        def dfs_mark(x, y, board):
            # 모든 O 부분을 #으로 마크
            board[x][y] = '#'
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                i = x+dx
                j = y+dy
                
                if i >= 0 and i<rows-1 and j>=0 and j<cols-1 and board[i][j] == 'O':
                    dfs_mark(i, j, board)
        
        # y가 0 or rows-1일 경우
        for i in [0, rows-1]:
            for j in range(cols):
                if board[i][j] == 'O':
                    dfs_mark(i, j, board)
        
        # x가 0 or cols-1일 경우
        for j in [0, cols-1]:
            for i in range(rows):
                if board[i][j] == 'O':
                    dfs_mark(i, j, board)
    
        
        # #이면 X로 못바꿈
        # 나머지는 X로 바꿈
        # 이게 왜 Union이냐 안쓰니 더 쉽네...
        for i in range(0, rows):
            for j in range(0, cols):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                        
                        