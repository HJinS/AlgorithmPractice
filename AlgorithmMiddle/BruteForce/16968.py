import math
in_str = input()

res = 0

for i in range(len(in_str)):
    if i == 0:
        if in_str[i] == 'd':
            res += 10
        else:
            res += 26
    elif in_str[i] == in_str[i-1]:
        if in_str[i] == 'd':
            res *= 9
        else:
            res *= 25
    else:
        if in_str[i] == 'd':
            res *= 10
        else:
            res *= 26
print(res)