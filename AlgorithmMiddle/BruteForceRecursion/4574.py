MAP = [[0 for i in range(9)] for j in range(9)]
row = [[False for i in range(10)] for j in range(9)]
col = [[False for i in range(10)] for j in range(9)]
square = [[[False for i in range(10)] for j in range(3)] for k in range(3)]
tile = [[False for i in range(10)] for j in range(10)]
flag = False
Tc = 1

def init():
    global MAP, row, col, square, tile, flag
    MAP = [[0 for i in range(9)] for j in range(9)]
    row = [[False for i in range(10)] for j in range(9)]
    col = [[False for i in range(10)] for j in range(9)]
    square = [[[False for i in range(10)] for j in range(3)] for k in range(3)]
    tile = [[False for i in range(10)] for j in range(10)]
    flag = False

def check(x, y, n1, n2, c):
    if c == 'H':
        if row[y][n1] or row[y][n2]:
            return False
        if col[x][n1] or col[x+1][n2]:
            return False
        if square[y//3][x//3][n1] or square[y//3][(x+1)//3][n2]:
            return False
        return True
    elif c == 'V':
        if row[y][n1] or row[y+1][n2]:
            return False
        if col[x][n1] or col[x][n2]:
            return False
        if square[y//3][x//3][n1] or square[(y+1)//3][x//3][n2]:
            return False
        return True

def makeVisit(x, y, n1, n2, c, t):
    tile[n1][n2] = t
    tile[n2][n1] = t

    if c == 'H':
        row[y][n1] = row[y][n2] = t
        col[x][n1] = col[x+1][n2] = t
        square[y//3][x//3][n1] = square[y//3][(x+1)//3][n2] = t

        if t == True:
            MAP[y][x] = n1
            MAP[y][x+1] = n2
        else:
            MAP[y][x] = MAP[y][x+1] = 0
    elif c == 'V':
        row[y][n1] = row[y+1][n2] = t
        col[x][n1] = col[x][n2] = t
        square[y//3][x//3][n1] = square[(y+1)//3][x//3][n2] = t

        if t == True:
            MAP[y][x] = n1
            MAP[y+1][x] = n2
        else:
            MAP[y][x] = MAP[y+1][x] = 0

def printMAP():
    for i in range(9):
        for j in range(9):
            print(MAP[i][j], end='')
        print()

def DFS(idx):
    global flag, Tc

    if flag:
        return
    if idx == 81:
        flag = True
        print("Puzzle", Tc)
        printMAP()
        return
    x = idx % 9
    y = idx //9

    if MAP[y][x] != 0:
        DFS(idx+1)
    else:
        if x <= 7 and MAP[y][x+1] == 0:
            for i in range(1, 10):
                for j in range(i+1, 10):
                    if not tile[i][j]:
                        if check(x, y, i, j, 'H'):
                            makeVisit(x, y, i, j, 'H', True)
                            DFS(idx + 2)
                            makeVisit(x, y, i, j, 'H', False)
                        if check(x, y, j, i, 'H'):
                            makeVisit(x, y, j, i, 'H', True)
                            DFS(idx + 2)
                            makeVisit(x, y, j, i, 'H', False)

        if y <= 7 and MAP[y+1][x] == 0:
            for i in range(1, 10):
                for j in range(i+1, 10):
                    if not tile[i][j]:
                        if check(x, y, i, j, 'V'):
                            makeVisit(x, y, i, j, 'V', True)
                            DFS(idx + 1)
                            makeVisit(x, y, i, j, 'V', False)
                        if check(x, y, j, i, 'V'):
                            makeVisit(x, y, j, i, 'V', True)
                            DFS(idx + 1)
                            makeVisit(x, y, j, i, 'V', False)

while True:
    N = int(input())
    if N == 0:
        break
    init()
    for i in range(N):
        n1, pos1, n2, pos2 = map(str, input().split())
        x1 = ord(pos1[1]) - ord('1')
        y1 = ord(pos1[0]) - ord('A')
        x2 = ord(pos2[1]) - ord('1')
        y2 = ord(pos2[0]) - ord('A')

        num1 = ord(n1) - ord('0')
        num2 = ord(n2) - ord('0')
        
        tile[num1][num2] = True
        tile[num2][num1] = True

        MAP[y1][x1] = num1
        MAP[y2][x2] = num2

        row[y1][num1] = True
        row[y2][num2] = True

        col[x1][num1] = True
        col[x2][num2] = True
        
        square[y1//3][x1//3][num1] = True
        square[y2//3][x2//3][num2] = True

    pos = list(map(str, input().split()))
    for i in range(1, 10):
        d = pos[i-1]
        x = ord(d[1]) - ord('1')
        y = ord(d[0]) - ord('A')

        row[y][i] = True
        col[x][i] = True
        square[y//3][x//3][i] = True
        MAP[y][x] = i
    
    DFS(0)

    Tc += 1

