N = int(input())
alpha = [0 for i in range(26)]
word_set = []

for i in range(N):
    word_set.append(input() )

for word in word_set:
    tmp = 0
    while word:
        now = word[-1]
        alpha[ord(now) - ord('A')] += pow(10, tmp)
        tmp += 1
        word = word[:-1]

alpha.sort(reverse=True)
res = 0

for i in range(9, 0, -1):
    res += alpha[9-i] * i
print(res)