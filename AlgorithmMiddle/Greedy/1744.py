N = int(input())
arr1 = []
arr2 = []
for i in range(N):
    num = int(input())
    if num > 0:
        arr1.append(num)
    else:
        arr2.append(num)

arr1.sort(reverse=True)
arr2.sort()

res = 0
cnt = 0
mul = 1
for n in arr1:
    if n == 1:
        res += n
    else:
        if cnt == 2:
            res += mul
            mul = 1
            cnt = 1
            mul *= n
        else:
            mul *= n
            cnt += 1
if cnt > 0:
    res += mul
mul = 1
cnt = 0
for n in arr2:
    if cnt == 2:
        res += mul
        mul = 1
        cnt = 1
        mul *= n
    else:
        mul *= n
        cnt += 1
if cnt > 0:
    res += mul 
 
print(res)