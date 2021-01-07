height = []
q = []
for i in range(9):
    height.append(int(input()))

total = sum(height)

for i in range(9):
    flag = False
    for j in range(9):
        if i != j:
            if total - height[i] - height[j] == 100:
                tmp1 = height[i]
                tmp2 = height[j]
                height.remove(tmp1)
                height.remove(tmp2)
                flag = True
                break
    if flag:
        break

height.sort()

for tmp in height:
    print(tmp)