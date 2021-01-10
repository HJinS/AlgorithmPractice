n = int(input())
candy = []

for i in range(n):
    candy.append(list(input()))

def check(i ,j):
    cnt1 = 1
    cnt2 = 1
    res = 1
    for k in range(n):
        if k < n-1 and candy[i][k] == candy[i][k+1]:
            cnt1 += 1
        else:
            res = max(res, cnt1)
            cnt1 = 1
            
    for k in range(n):
        if k < n-1 and candy[k][j] == candy[k+1][j]:
            cnt2 += 1
        else:
            res = max(res, cnt2)
            cnt2 = 1
    return res

def swap(i, j, k, l):
    tmp = candy[i][j]
    candy[i][j] = candy[k][l]
    candy[k][l] = tmp

res = 0

for i in range(n):
    for j in range(n-1):
        swap(i, j, i, j+1)
        res = max(res, check(i,j))
        swap(i, j, i, j+1)

        swap(j, i, j+1, i)
        res = max(res, check(j, i))
        swap(j, i, j+1, i)

for i in range(n):
    for j in range(1, n):
        swap(i, j, i, j-1)
        res = max(res, check(i,j))
        swap(i, j, i, j-1)

        swap(j, i, j-1, i)
        res = max(res, check(j, i))
        swap(j, i, j-1, i)

print(res)
