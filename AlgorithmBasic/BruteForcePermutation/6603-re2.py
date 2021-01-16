import sys
k = 0
inputArr = []
arr = []
res = [-1 for i in range(6)]
visited = [False for i in range(14)]
def comb(start, cnt):
    if cnt == 6:
        for i in range(6):
            print(res[i], end=' ')
        print()
        return
    for i in range(start, k):
        if visited[i] == False:
            visited[i] = True
            res[cnt] = arr[i]
            comb(i, cnt+1)
            visited[i] = False


while True:
    inputArr = list(map(int, input().split()))
    k = inputArr[0]
    arr = inputArr[1:]
    if k == 0:
        sys.exit()
    arr.sort()
    comb(0,0)
    print()