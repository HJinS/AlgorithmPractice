from collections import deque
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 키워드는 데이터의 구조를 어떻게 정할지
        # 여기서는 row, column, box를 나누어서 따로 저장
        # 몇번째 row에 어떤 숫자가 있는지 없는지
        r = [[False for i in range(10)] for i in range(9)] # r0 1 True/False
        c = [[False for i in range(10)] for i in range(9)]
        b = [[False for i in range(10)] for i in range(9)] # grid
        
        def available(x, y, n):
            boxno = x // 3 * 3 + y // 3
            return not r[x][n] and not c[y][n] and not b[boxno][n]
        
        tofill = deque()
        # 초기화 - 채워야 할 칸의 index를 tofill에 넣음
        # 이미 숫자가 있는 경우에는 각각의 box, row, column배열에 표기
        for x in range(9):
            for y in range(9):
                n = board[x][y]
                if n == '.':
                    tofill.append((x, y))
                else:
                    n = int(n)
                    boxno = x // 3 * 3 + y // 3 
                    r[x][n] =  c[y][n] = b[boxno][n] = True
                   
        tofill = list(tofill)
        def dfs(index):
            if index == len(tofill):
                return True
            x, y  = tofill[index]
            boxno = x // 3 * 3 + y // 3
            
            for n in range(1, 10):
                if not available(x, y ,n): 
                    continue
                board[x][y] = str(n)
                r[x][n] =  c[y][n] = b[boxno][n] = True
                # 숫자를 넣고 다음 인덱스도 True이면 True 반환
                # 브루트포스
                if dfs(index + 1):
                    return True
                # 숫자 빼고 다음 숫자 확인
                board[x][y] = '.'
                r[x][n] =  c[y][n] = b[boxno][n] = False
            return False

        dfs(0)