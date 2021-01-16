import sys
N = int(input())
arr = list(input())
s = [['-1' for i in range(N)] for j in range(N)]
num = []
res = [0 for i in range(N)]

cnt = 0
flag = False
for i in range(N):
    for j in range(N):
        if i <= j:
            s[i][j] = arr[cnt]
            cnt += 1
        if cnt >= N * (N + 1) // 2:
            flag = True
    if flag:
        break
for i in range(-10,11):
    num.append(i)

def solve(cnt):
    if cnt == N:
        for i in range(N):
            print(res[i],end=' ')
        print()
        sys.exit()
    sum = 0
    for i in range(21):
        res[cnt] = num[i]
        right = 0
        for j in  range(cnt+1):
            sum = 0
            for k in range(j,cnt+1):
                sum += res[k]
            if sum < 0 and s[j][cnt] == '-':
                right += 1
            elif sum > 0 and s[j][cnt] == '+':
                right += 1
            elif sum == 0 and s[j][cnt] == '0':
                right += 1
        if right == cnt+1:
            solve(cnt + 1)
solve(0)

                
