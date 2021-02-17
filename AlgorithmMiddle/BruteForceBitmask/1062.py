N, K = map(int, input().split())
words = []
checked = [0 for i in range(26)]
res = 0
for i in range(N):
    words.append(input())

def solve(index, cnt):
    global res
    if cnt == K-5:
        checked_cnt = 0
        
        for word in words:
            flag = False
            for w in word:
                if not checked[ord(w) - ord('a')]:
                    flag = True
                    break
            if not flag:
                checked_cnt += 1
        res = max(checked_cnt, res)
    
    for i in range(index, 26):
        if not checked[i]:
            checked[i] = True
            solve(i, cnt+1)
            checked[i] = False

for c in ['a', 'c', 'i', 'n', 't']:
    checked[ord(c) - ord('a')] = True

if K < 5:
    print(0)
else:
    solve(0, 0)
    print(res)