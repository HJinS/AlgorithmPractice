input_str = input()

res = 0

for i in range(len(input_str)):
    if i == 0:
        if input_str[i] == 'd':
            res += 10
        elif input_str[i] == 'c':
            res += 26
    elif input_str[i] == input_str[i-1]:
        if input_str[i] == 'd':
            res *= 9
        elif input_str[i] == 'c':
            res *= 25
    else:
        if input_str[i] == 'd':
            res *= 10
        elif input_str[i] == 'c':
            res *= 26
print(res)