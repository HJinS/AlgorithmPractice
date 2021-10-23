import sys
def solution(rows, columns, queries):
    board = [[(j-1)*columns+i for i in range(1, columns+1)] for j in range(1, rows+1)]
    ans = []
    def rotate(x1, y1, x2, y2):
        nonlocal board, ans
        MIN = sys.maxsize
        i, j = x1, y1
        tmp1 = board[i][j]
        tmp2 = board[i][j+1]
        while j < y2:
            tmp2 = board[i][j+1]
            board[i][j+1] = tmp1
            tmp1 = tmp2
            MIN = min(tmp1, MIN)
            j += 1
        while i < x2:
            tmp2 = board[i+1][j]
            board[i+1][j] = tmp1
            tmp1 = tmp2
            MIN = min(tmp1, MIN)
            i += 1
        while j > y1:
            tmp2 = board[i][j-1]
            board[i][j-1] = tmp1
            tmp1 = tmp2
            MIN = min(tmp1, MIN)
            j -= 1
        while i > x1:
            tmp2 = board[i-1][j]
            board[i-1][j] = tmp1
            tmp1 = tmp2
            MIN = min(tmp1, MIN)
            i -= 1
        ans.append(MIN)
        
    for q in queries:
        rotate(q[0]-1, q[1]-1, q[2]-1, q[3]-1)
    return ans