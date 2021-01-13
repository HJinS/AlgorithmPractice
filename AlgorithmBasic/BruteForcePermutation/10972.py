import sys
n = int(input())

arr = list(map(int, input().split()))

tmp_i = n-1
tmp = arr[n-1]

for i in range(n-1,0,-1):
    if arr[i-1] < arr[i]:
        tmp_i = i-1
        tmp = arr[i-1]
        break

if tmp_i == n-1:
    print(-1)
    sys.exit()

for i in range(n-1,tmp_i, -1):
    if tmp < arr[i]:
        temp = arr[tmp_i]
        arr[tmp_i] = arr[i]
        arr[i] = temp
        break


arr1 = arr[:tmp_i+1]
arr2 = arr[tmp_i+1:]
arr2.sort()
arr1.extend(arr2)

for i in range(n):
    print(arr1[i],end=' ')
print()