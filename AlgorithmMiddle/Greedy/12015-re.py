N = int(input())
arr = list(map(int, input().split()))
lis = [0 for i in range(N)]

def solve():
    lis[0] = arr[0]
    back = 0
    for i in range(N):
        if lis[back] < arr[i]:
            back += 1
            lis[back] = arr[i]
        else:
            l, r = 0, back
            while l < r:
                mid = int((l + r) // 2)
                if lis[mid] < arr[i]:
                    l = mid + 1
                else:
                    r = mid
            lis[r] = arr[i]
    print(back+1)
solve()