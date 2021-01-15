L, C = map(int, input().split())

arr = list(map(str, input().split()))
res = ['0' for i in range(L)]
visited = [False for i in range(C)]

vowel = ['a','e','i','o','u']

arr.sort()

def comb(cnt, cnt1, cnt2):
    if cnt == L:
        if cnt1 >= 1 and cnt2 >= 2:
            for i in range(L):
                print(res[i], end='')
            print()
        return
        
    
    for i in range(C):
        if visited[i] == False and (cnt == 0 or res[cnt - 1] < arr[i]):
            visited[i] = True
            if cnt == 0:
                cnt1 = 0
                cnt2 = 0
            if arr[i] in vowel:
                cnt1 += 1
            else:
                cnt2 += 1
            res[cnt] = arr[i]
            comb(cnt + 1, cnt1, cnt2)
            if arr[i] in vowel:
                cnt1 -= 1
            else:
                cnt2 -= 1
            visited[i] = False

comb(0,0,0)