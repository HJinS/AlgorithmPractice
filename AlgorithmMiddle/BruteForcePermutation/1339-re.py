N = int(input())
pri = [0 for i in range(26)]
for i in range(N):
    word = input()
    
    tmp = 1
    for s in range(len(word)-1, -1, -1):
        pri[ord(word[s]) - ord('A')] += tmp
        tmp *= 10

pri.sort(reverse=True)

res = 0
for i in range(9, 0, -1):
    res += pri[9-i] * i
print(res)

