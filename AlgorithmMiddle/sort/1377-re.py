n = int(input())
arr = []
for i in range(n):
    arr.append([int(input()), i])
sorted_arr = sorted(arr)

res = 0
for i in range(n):
    res = max(res, sorted_arr[i][1] - i)
print(res+1)
