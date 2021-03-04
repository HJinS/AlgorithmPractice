N = int(input())

arr = list(map(int, input().split()))

lis = [0 for i in range(N)]
res = 0
def LIS():
    global res
    lis[0] = arr[0]
    back = 0
    for i in range(N):
        if lis[back] < arr[i]:
            back += 1
            lis[back] = arr[i]
        else:
            l = 0
            r = back
            while l < r:
                mid = int((l + r) // 2)
                if lis[mid] < arr[i]:
                    l = mid + 1
                else:
                    r = mid
            lis[r] = arr[i]
    res = back + 1

LIS()
print(res)