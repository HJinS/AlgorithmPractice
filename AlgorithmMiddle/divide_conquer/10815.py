N = int(input())
cards = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))
res = [-1 for i in range(M)]
cards.sort()
def solve(num_idx):
    l, r = 0, N-1
    while l <= r:
        mid = int((l+r)//2)
        if cards[mid] > num[num_idx]:
            r = mid-1
        elif cards[mid] < num[num_idx]:
            l = mid+1
        elif cards[mid] == num[num_idx]:
            res[num_idx] = 1
            return
    res[num_idx] = 0

for i in range(M):
    solve(i)
for i in range(M):
    print(res[i], end=' ')