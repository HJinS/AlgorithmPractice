N, K = map(int, input().split())
words = []
checked = [False for i in range(26)]
flag = False
res = 0

for i in range(N):
    words.append(list(input()))


def solve(index, cnt):
    global K, flag, res

    if cnt == K-5:
        words_cnt = 0
        for word in words:
            flag = False
            for w in word:
                if not checked[ord(w) - ord('a')]:
                    flag = True
                    break
            if not flag:
                words_cnt += 1
        res = max(res, words_cnt)
    
    for i in range(index, 26):
        if not checked[i]:
            checked[i] = True
            solve(i, cnt+1)
            checked[i] = False


for i in ['a', 'n', 't', 'i', 'c']:
    checked[ord(i) - ord('a')] = True

solve(0, 0)
print(res)

