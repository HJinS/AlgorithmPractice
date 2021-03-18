N = int(input())
sum = 1
def hanoi(start, middle, des, cnt):
    if cnt == 1:
        print(start, des)
        return
    else:
        hanoi(start, des, middle, cnt-1)
        print(start, des)
        hanoi(middle, start, des, cnt-1)

print(2**N-1)
hanoi(1,2,3,N)