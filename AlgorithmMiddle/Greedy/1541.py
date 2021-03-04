from sys import stdin
import re

exp = input()
arr = re.findall("\d+", exp)
op = []
num = []
for c in exp:
    if c == "+" or c == "-":
        op.append(c)
for c in arr:
    num.append(int(c))

flag = False
res = num[0]
for i in range(len(op)):
    if op[i] == '-':
        flag = True
        res -= num[i+1]
    else:
        if flag:
            res -= num[i+1]
        else:
            res += num[i+1]

print(res)