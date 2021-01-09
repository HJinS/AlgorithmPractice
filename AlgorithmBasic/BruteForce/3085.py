n = int(input())
candy = []
for i in range(n):
    candy.append(list(input()))


def swap(i, j, k, l):
    tmp = candy[i][j]
    candy[i][j] = candy[k][l]
    candy[k][l] = tmp

def numOfCandy():
    res = 1
    for i in range(n):
        tmp = 1
        for j in range(1, n):
            if candy[i][j-1] == candy[i][j]:
                tmp += 1
            else:
                res = max(res, tmp)
                tmp = 1
        res=  max(res,tmp)
    for i in range(n):
        tmp = 1
        for j in range(n-1):
            if candy[j+1][i] == candy[j][i]:
                tmp += 1
            else:
                res = max(res, tmp)
                tmp = 1
        res=  max(res,tmp)
    return res

res = 0

for i in range(n):
    for j in range(n-1):
        swap(i,j,i,j+1)
        res = max(res, numOfCandy())
        swap(i,j,i,j+1)

        swap(j,i,j+1,i)
        res = max(res, numOfCandy())
        swap(j,i,j+1,i)
print(res)