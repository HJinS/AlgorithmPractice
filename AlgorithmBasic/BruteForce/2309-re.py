height = []
for i in range(9):
    height.append(int(input()))

total = sum(height)

for i in range(9):
    flag = False
    for j in range(9):
        if i != j:
            
            if total - height[i] - height[j] == 100:
                non1 = height[i]
                non2 = height[j]
                height.remove(non1)
                height.remove(non2)
                flag = True
                break
    if flag:
        break

height.sort()
for i in range(len(height)):
    print(height[i])