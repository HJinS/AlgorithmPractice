N = int(input())
arr = []
for i in range(N):
    arr.append([int(input()), i])

sorted_arr = sorted(arr)

ans = []
for i in range(N):
    ans.append(sorted_arr[i][1] - i)

print(max(ans) + 1)