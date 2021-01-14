import sys

N = int(input())
arr = list(map(int, input().split()))

tmp = arr[N-1]
tmp_i = N-1

for i in range(N-1,0,-1):
    if arr[i-1] < arr[i]:
        tmp = arr[i-1]
        tmp_i = i-1
        break

if tmp_i == N-1:
    print(-1)
    sys.exit()

for i in range(N-1,tmp_i,-1):
    if tmp < arr[i]:
        temp = arr[i]
        arr[i] = arr[tmp_i]
        arr[tmp_i] = temp
        break

arr1 = arr[:tmp_i+1]
arr2 = arr[tmp_i+1:]
arr2.sort()
arr1.extend(arr2)

for i in range(N):
    print(arr1[i],end=' ')