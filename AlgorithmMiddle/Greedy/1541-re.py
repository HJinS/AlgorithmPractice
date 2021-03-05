import re

exp = input()
num = re.findall("\d+", exp)
arr = []
op = []
for c in exp:
    if c == "+" or c == "-":
        op.append(c)

for n in num:
    arr.append(int(n))

flag = False
res = 0
res = arr[0]
for i in range(len(op)):
    if op[i] == "-":
        res -= arr[i+1]
        flag = True
    else:
        if flag:
            res -= arr[i+1]
        else:
            res += arr[i+1]
print(res)
