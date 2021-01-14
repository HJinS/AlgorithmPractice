res = [0 for i in range(6)]
inputArr = []
k = 0
arr = []
visited = [False for i in range(13)]

def comb(start, cnt):
    if cnt == 6:
        for i in range(6):
            print(res[i], end=' ')
        print()
        return
    
    for i in range(start,k):
        if visited[i] == False:
            visited[i] = True
            res[cnt] = arr[i]
            comb(i+1, cnt + 1)
            visited[i] = False

while True:
    inputArr = list(map(int, input().split()))
    k = inputArr[0]
    arr = inputArr[1:]
    arr.sort()
    if k == 0:
        break
    comb(0,0)
    print()

