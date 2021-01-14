n = int(input())

arr = list(map(int, input().split()))
visited = [False for i in range(n)]
res = [0 for i in range(n)]

global sumMax
sumMax = 0

arr.sort()


def permu(cnt):
    global sumMax
    if cnt == n:
        sum = 0
        for i in range(1,n):
            sum += abs(res[i-1] - res[i])
        sumMax = max(sumMax, sum)

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            res[cnt] = arr[i]
            permu(cnt + 1)
            visited[i] = False
permu(0)
print(sumMax)