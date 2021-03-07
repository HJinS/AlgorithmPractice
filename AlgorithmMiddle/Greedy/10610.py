import sys
n = list(input())
n.sort(reverse=True)

sum_digit = 0
for i in range(len(n)):
    sum_digit += int(n[i])
if n[len(n)-1] == '0':
    if sum_digit % 3 == 0:
        print("".join(n))
    else:
        print(-1)
else:
    print(-1)